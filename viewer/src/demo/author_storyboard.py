"""Reproducible shooting score. Run from any directory after editing the script."""
import json
from datetime import datetime
from pathlib import Path

shots = []
p = {}

def shot(chapter, duration, title, caption, camera, end=None, focus='scene', focus_end=None,
         solar='off', sliders=None, metric='illuminance', quality='preview', hour=12, timestep=None, **changes):
    global p
    p = {**p, **changes}
    shots.append(dict(chapter=chapter, duration=duration, title=title, caption=caption,
        detail='', overview=None, camera=camera, cameraEnd=end or camera, focus=focus, focusEnd=focus_end or focus,
        solar=solar, sliders=sliders or [], metric=metric, quality=quality, hour=hour,
        timestep=timestep if timestep is not None else 171*24+hour, parameters=p.copy()))

def sweep(chapter, duration, title, caption, start_camera, end_camera, target, steps=10, **options):
    start = p.copy()
    defaults = {'width':6,'depth':9,'height':3,'window_width':3,'window_offset':0,'window_height':1.5,
        'sill_height':1,'overhang_depth':.75,'left_fin_depth':.5,'right_fin_depth':.5,
        'glazing_transmittance':.6,'wall_reflectance':.7,'floor_reflectance':.2,'ceiling_reflectance':.8,
        'shade_reflectance':.5,'notch_width':0,'notch_depth':0,'context_height':0,'context_offset':0,
        'context_distance':4,'sensor_spacing':.5,'workplane_height':.75}
    for i in range(steps):
        a, b = i/steps, (i+1)/steps
        values = {k: round(start.get(k, defaults.get(k, 0))+(v-start.get(k, defaults.get(k, 0)))*b, 4) for k,v in target.items()}
        cam = [x+(y-x)*a for x,y in zip(start_camera,end_camera)]
        end = [x+(y-x)*b for x,y in zip(start_camera,end_camera)]
        shot(chapter,duration/steps,title,caption,cam,end,**options,**values)

shot('Foton', 1.5, 'Foton', 'Annual daylight analysis on the GPU.', [-48,26,1.8], [-10,30,1.8], focus='facade', quality='final')
shot('Foton', 2.5, 'Interactive daylight analysis', 'Change the design and the whole year is recalculated.', [-10,30,1.8], [48,52,1.8], focus='facade',focus_end='scene')
sweep('Parameters',3,'Window geometry', 'Change window width and position.',[48,52,1.8],[-35,38,1.8],
      {'window_width':1.1,'window_offset':-1.8,'overhang_depth':0,'left_fin_depth':0,'right_fin_depth':0},sliders=['window_width','window_offset','overhang_depth'])
sweep('Parameters',3,'Shading devices', 'Adjust window height, overhangs and side fins.',[-35,38,1.8],[35,28,1.8],
      {'window_offset':1.8,'window_height':2.2,'sill_height':.4,'overhang_depth':1.8,'left_fin_depth':1.1,'right_fin_depth':1.1},sliders=['window_offset','window_height','overhang_depth'])
shot('Parameters',1.5,'Multiple windows', 'Add openings to the façade.',[35,28,1.8],[0,50,1.8],window_count=3,window_width=1.4,window_offset=0,sliders=['window_width','overhang_depth','glazing_transmittance'])
sweep('Parameters',2.5,'Material properties', 'Vary glazing transmittance and surface reflectance.',[0,50,1.8],[-48,58,1.8],
      {'glazing_transmittance':.85,'wall_reflectance':.9,'floor_reflectance':.55,'ceiling_reflectance':.95,'shade_reflectance':.85,'overhang_depth':.3},sliders=['glazing_transmittance','wall_reflectance','floor_reflectance'])
sweep('Room geometry',3,'Room dimensions', 'Change room width, depth and height.',[-48,58,1.8],[20,78,1.8],{'width':12,'depth':14,'height':4},sliders=['width','depth','height'])
sweep('Room geometry',4,'L-shaped room', 'Recalculate daylight as the floor plan changes.',[20,78,1.8],[-30,84,1.8],{'notch_width':7,'notch_depth':8},steps=12,sliders=['notch_width','notch_depth','width'])
shot('Room geometry',2,'Sensor grid', 'Change sensor spacing and workplane height.',[-30,84,1.8],[-65,46,1.8],sensor_spacing=.8,workplane_height=1,quality='final',metric='df',sliders=['sensor_spacing','workplane_height','notch_width'])
p={'context_distance':1.5, 'context_offset':-4}
sweep('Context shading',3,'Context shading', 'Include a neighbouring building in the calculation.',[-65,46,1.8],[-130,48,1.8],{'context_height':6},sliders=['context_height','context_distance','context_offset'])
sweep('Context shading',3,'Combined shading', 'Move the building and adjust its height and the overhang.',[-130,48,1.8],[-235,44,1.8],{'context_height':3,'context_offset':8,'overhang_depth':1.8},sliders=['context_height','context_offset','overhang_depth'])
p={}
for i,hour in enumerate(range(7,19)):
    shot('Hourly analysis',.5,'Hourly daylight', 'Gothenburg weather · 21 June · 07:30–18:30', [125-i*12,44,1.8],[113-i*12,44,1.8],solar='day',hour=hour,quality='final')
for month in range(1,13):
    timestep=int((datetime(2025,month,21,12)-datetime(2025,1,1)).total_seconds()/3600)
    shot('Annual analysis',.5,'Seasonal sun paths', 'Monthly paths and the sun’s position at noon through the year.',[-43+(month-1)*5,40,1.8],[-38+(month-1)*5,45,1.8],solar='year',timestep=timestep,quality='final')
for metric,duration,title,caption in [('df',2.5,'Daylight factor','Indoor / outdoor illuminance under an overcast sky.'),('da',3,'Daylight autonomy','Share of occupied hours with at least 300 lux at each sensor.'),('sda',3,'Spatial daylight autonomy','Area with at least 300 lux for half the occupied hours · static shades.')]:
    shot('Annual analysis',duration,title,caption,[17,45,1.8],[{'df':35,'da':55,'sda':75}[metric],52,1.8],solar='year',metric=metric,quality='final')
shot('Open source',5,'Daylight analysis for Grasshopper and Python', 'pip install foton-daylight · or one toggle in Grasshopper',[75,52,1.8],[100,46,1.8],metric='da',quality='final')
# Every move begins exactly where the preceding move finishes. Unwrap azimuth
# at +/-180 degrees so a boundary never produces a full reverse revolution.
for previous, current in zip(shots, shots[1:]):
    current['camera'] = previous['cameraEnd'].copy()
    start = current['camera'][0]
    current['cameraEnd'][0] = start + (current['cameraEnd'][0] - start + 180) % 360 - 180
for chapter in ['Parameters', 'Context shading']:
    [s for s in shots if s['chapter'] == chapter][-1]['quality'] = 'final'
shots[-1]['detail']='MIT licence · Honeybee models in, Ladybug heatmaps out'
TOTAL = 54.5
assert abs(sum(s['duration'] for s in shots)-TOTAL)<1e-6
Path(__file__).with_name('storyboard.json').write_text(json.dumps(shots,indent=2)+'\n')
print(f'{len(shots)} shots / {sum(s["duration"] for s in shots):.1f} seconds')

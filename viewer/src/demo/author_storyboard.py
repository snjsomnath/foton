"""Reproducible shooting score. Run from any directory after editing the script."""
import json
import math
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

shot('Foton', 2, 'Foton', 'GPU light transport for daylight teaching.', [-48,26,1.8], [12,32,1.8], focus='facade', quality='final')
shot('Foton', 3, 'Interactive daylight analysis', 'Fast GPU calculations support parametric exploration.', [12,32,1.8], [48,52,1.8], focus='facade',focus_end='scene')
sweep('Parameters',3,'Window geometry', 'Change window width and position.',[48,52,1.8],[-35,38,1.8],
      {'window_width':1.1,'window_offset':-1.8,'overhang_depth':0,'left_fin_depth':0,'right_fin_depth':0},sliders=['window_width','window_offset','overhang_depth'])
sweep('Parameters',3,'Shading devices', 'Adjust window height, overhangs and side fins.',[-35,38,1.8],[35,28,1.8],
      {'window_offset':1.8,'window_height':2.2,'sill_height':.4,'overhang_depth':1.8,'left_fin_depth':1.1,'right_fin_depth':1.1},sliders=['window_offset','window_height','overhang_depth'])
shot('Parameters',1,'Multiple windows', 'Add openings to the façade.',[35,28,1.8],[0,50,1.8],window_count=3,window_width=1.4,window_offset=0,sliders=['window_width','overhang_depth','glazing_transmittance'])
sweep('Parameters',3,'Material properties', 'Vary glazing transmittance and surface reflectance.',[0,50,1.8],[-48,58,1.8],
      {'glazing_transmittance':.85,'wall_reflectance':.9,'floor_reflectance':.55,'ceiling_reflectance':.95,'shade_reflectance':.85,'overhang_depth':.3},sliders=['glazing_transmittance','wall_reflectance','floor_reflectance'])
sweep('Room geometry',3,'Room dimensions', 'Change room width, depth and height.',[-48,58,1.8],[20,78,1.8],{'width':12,'depth':14,'height':4},sliders=['width','depth','height'])
sweep('Room geometry',4,'L-shaped room', 'Recalculate daylight as the floor plan changes.',[20,78,1.8],[-30,84,1.8],{'notch_width':7,'notch_depth':8},steps=12,sliders=['notch_width','notch_depth','width'])
shot('Room geometry',2,'Sensor grid', 'Change sensor spacing and workplane height.',[-30,84,1.8],[-65,46,1.8],sensor_spacing=.8,workplane_height=1,quality='final',metric='df',sliders=['sensor_spacing','workplane_height','notch_width'])
p={'context_distance':1.5, 'context_offset':-4}
sweep('Context shading',3,'Context shading', 'Include a neighbouring building in the calculation.',[-65,46,1.8],[-120,48,1.8],{'context_height':6},sliders=['context_height','context_distance','context_offset'])
sweep('Context shading',3,'Obstruction position', 'Move the neighbouring building relative to the windows.',[-120,48,1.8],[-190,55,1.8],{'context_offset':0,'overhang_depth':0},sliders=['context_height','context_offset','overhang_depth'])
sweep('Context shading',3,'Combined shading', 'Adjust the building height, position and overhang.',[-190,55,1.8],[-235,44,1.8],{'context_height':3,'context_offset':8,'overhang_depth':1.8},sliders=['context_height','context_offset','overhang_depth'])
p={}
for i,hour in enumerate(range(7,19)):
    shot('Hourly analysis',8/12,'Hourly daylight', 'Gothenburg weather · 21 June · 07:30–18:30', [125-i*12,44,1.8],[113-i*12,44,1.8],solar='day',hour=hour,quality='final')
for month in range(1,13):
    timestep=int((datetime(2025,month,21,12)-datetime(2025,1,1)).total_seconds()/3600)
    shot('Annual analysis',.4,'Seasonal sun paths', 'Monthly paths and the sun’s position at noon through the year.',[-43+(month-1)*5,40,1.8],[-38+(month-1)*5,45,1.8],solar='year',timestep=timestep,quality='final')
for metric,duration,title,caption in [('df',1.6,'Daylight factor','Indoor / outdoor illuminance under an overcast sky.'),('da',1.8,'Daylight autonomy','Share of occupied hours with at least 300 lux at each sensor.'),('sda',1.8,'Spatial daylight autonomy','Area with at least 300 lux for half the occupied hours · static shades.')]:
    shot('Annual analysis',duration,title,caption,[17,45,1.8],[{'df':35,'da':55,'sda':75}[metric],52,1.8],solar='year',metric=metric,quality='final')
p={}
shot('Multiple zones',1.5,'Multiple-zone analysis', 'Increase the number of rooms in the model.',[45,60,1.8],[15,48,1.8],sensor_spacing=1.5)
for count in [16,64,256]:
    shot('Multiple zones',1.5,f'{count:,} zones', 'GPU transport with independent sensor grids.',[15,48,1.8],[35,62,1.8],room_count=count,focus='scene')
shot('Multiple zones',8,'1,024 zones', '24,576 sensor cells calculated on the GPU.',[35,48,1.8],[-15,62,1.8],focus='scene',focus_end='scene',room_count=1024)
# Widen before the next group arrives, then hold that framing through its GPU wait.
# These bounds use the default room and the demo's wide instance layout; the
# backend geometry test checks every authored bound against the actual vertices.
def campus_bounds(count):
    columns = min(count, math.ceil(math.sqrt(count) * 2))
    rows = math.ceil(count / columns)
    return [[0, -.75, 0], [6 + (columns - 1) * 9, 9 + (rows - 1) * 12.75, 3]]

scale_shots = [s for s in shots if s['chapter'] == 'Multiple zones']
for i, current in enumerate(scale_shots):
    count = current['parameters'].get('room_count', 1)
    next_count = scale_shots[min(i + 1, len(scale_shots) - 1)]['parameters'].get('room_count', 1)
    current['overview'] = {'from': campus_bounds(count), 'to': campus_bounds(next_count),
                           'leadIn': 0 if i == 0 else .5}
shot('Open source',7,'Open-source daylight simulation', 'Fast GPU light transport for parametric daylight teaching.',[-15,62,1.8],[12,48,1.8])
# Every move begins exactly where the preceding move finishes. Unwrap azimuth
# at +/-180 degrees so a boundary never produces a full reverse revolution.
for previous, current in zip(shots, shots[1:]):
    current['camera'] = previous['cameraEnd'].copy()
    start = current['camera'][0]
    current['cameraEnd'][0] = start + (current['cameraEnd'][0] - start + 180) % 360 - 180
for chapter in ['Parameters', 'Context shading']:
    [s for s in shots if s['chapter'] == chapter][-1]['quality'] = 'final'
shots[-1]['detail']='MIT licence · Source code available on GitHub'
assert abs(sum(s['duration'] for s in shots)-72)<1e-6
Path(__file__).with_name('storyboard.json').write_text(json.dumps(shots,indent=2)+'\n')
print(f'{len(shots)} shots / {sum(s["duration"] for s in shots):.0f} seconds')

# Architectural daylight sample models

Generated fixtures; numerical acceptance requires the Radiance comparison suite.

| Scene | Category | Architectural question |
| --- | --- | --- |
| [sealed](sealed.hbjson) | controls | Does a completely enclosed room remain dark? |
| [black_open](black_open.hbjson) | controls | Is direct sky integration correct without glazing or reflections? |
| [coloured_glass](coloured_glass.hbjson) | materials | Does tinted glass preserve RGB transport and photopic conversion? |
| [overhang_fins](overhang_fins.hbjson) | shading | How do combined overhangs and side fins mask the sky? |
| [deep_reflective](deep_reflective.hbjson) | materials | Does reflected light reach the rear of a deep bright room? |
| [rooflit](rooflit.hbjson) | openings | How does a roof opening illuminate the workplane? |
| [context_obstruction](context_obstruction.hbjson) | context | How much sky does a neighbouring facade obstruct? |
| [interior_glazing](interior_glazing.hbjson) | connections | Does daylight pass through a shared glazed wall exactly once? |
| [irregular](irregular.hbjson) | form | Is an L-shaped room triangulated without filling its recess? |
| [acceptance](acceptance.hbjson) | integration | Does the classroom and two-office model retain its Honeybee results? |
| [side_lit_reference](side_lit_reference.hbjson) | controls | What is the clear-glazed south-facing reference room? |
| [shallow_plan](shallow_plan.hbjson) | form | How evenly does side lighting illuminate a shallow room? |
| [narrow_corridor](narrow_corridor.hbjson) | form | How far does end-window light travel down a narrow corridor? |
| [double_height](double_height.hbjson) | form | How does tall glazing light a double-height volume? |
| [pitched_roof](pitched_roof.hbjson) | form | Do sloped roof surfaces reflect light correctly beneath a ridge? |
| [trapezoid_plan](trapezoid_plan.hbjson) | form | How do splayed walls change illumination and reflections? |
| [u_shaped_plan](u_shaped_plan.hbjson) | form | Do the wings of a U-shaped room occlude one another? |
| [north_facing](north_facing.hbjson) | orientation | Is north-facing glazing assigned to the correct sky patches? |
| [east_facing](east_facing.hbjson) | orientation | Is east-facing glazing assigned to the correct sky patches? |
| [west_facing](west_facing.hbjson) | orientation | Is west-facing glazing assigned to the correct sky patches? |
| [rotated_37](rotated_37.hbjson) | orientation | Does an oblique room retain its glazing, shades and grids? |
| [corner_glazing](corner_glazing.hbjson) | openings | How do windows on adjacent facades combine at a corner? |
| [opposite_glazing](opposite_glazing.hbjson) | openings | How does glazing on opposite facades balance daylight? |
| [ribbon_windows](ribbon_windows.hbjson) | openings | Do separated ribbon openings retain their opaque mullion gaps? |
| [clerestory](clerestory.hbjson) | openings | How does a high narrow opening distribute light toward the ceiling? |
| [full_height_glazing](full_height_glazing.hbjson) | openings | Is large near-floor glazing represented without edge leaks? |
| [multiple_rooflights](multiple_rooflights.hbjson) | openings | How do four separated rooflights combine across the workplane? |
| [rooflight_well](rooflight_well.hbjson) | shading | How does a one-metre-deep opaque shaft below a rooflight restrict the sky? |
| [deep_overhang](deep_overhang.hbjson) | shading | How does a deep overhang exclude high sky while retaining low sky? |
| [asymmetric_fins](asymmetric_fins.hbjson) | shading | Do unequal fins produce different east and west sky masks? |
| [horizontal_louvres](horizontal_louvres.hbjson) | shading | Do repeated tilted horizontal blades preserve narrow sky gaps? |
| [vertical_louvres](vertical_louvres.hbjson) | shading | How do repeated vertical blades screen oblique sky directions? |
| [eggcrate](eggcrate.hbjson) | shading | How do intersecting vertical and horizontal blades combine? |
| [light_shelf](light_shelf.hbjson) | shading | Does a shelf block direct light and reflect light toward the ceiling? |
| [balcony_above](balcony_above.hbjson) | shading | How does an upper balcony slab shade a full-width facade? |
| [recessed_window](recessed_window.hbjson) | shading | How do deep opaque window reveals screen low and oblique sky? |
| [urban_canyon](urban_canyon.hbjson) | context | How do tall buildings on both sides restrict side lighting? |
| [courtyard_context](courtyard_context.hbjson) | context | How does enclosing context restrict a room's courtyard view? |
| [offset_tower](offset_tower.hbjson) | context | Does an off-axis tall obstruction affect the appropriate sky sectors? |
| [reflective_neighbour](reflective_neighbour.hbjson) | context | Does a bright neighbouring facade contribute reflected daylight? |
| [dark_interior](dark_interior.hbjson) | materials | How does a dark finish suppress indirect illumination? |
| [bright_ceiling](bright_ceiling.hbjson) | materials | How much does changing only ceiling reflectance redistribute light? |
| [coloured_walls](coloured_walls.hbjson) | materials | Do coloured diffuse walls preserve RGB reflected transport? |
| [low_transmittance](low_transmittance.hbjson) | materials | Does low-transmittance glass attenuate light without turning opaque? |
| [mixed_glazing](mixed_glazing.hbjson) | materials | Are adjacent windows with different glass properties kept distinct? |
| [three_room_chain](three_room_chain.hbjson) | connections | Can daylight cross two successive internal glass partitions? |
| [glazed_corridor](glazed_corridor.hbjson) | connections | Does a glazed corridor feed an office and an adjoining meeting room? |
| [stacked_rooms](stacked_rooms.hbjson) | connections | Does an opaque shared slab isolate two storeys? |
| [courtyard_rooms](courtyard_rooms.hbjson) | connections | Do four inward-facing rooms shade one another beneath a pergola? |
| [atrium_borrowed_light](atrium_borrowed_light.hbjson) | connections | Can a rooflit atrium feed rooms at two levels through internal glass? |
| [plan_i_small_center](plan_i_small_center.hbjson) | form | How does a small center opening illuminate a I-shaped plan? |
| [plan_i_large_center](plan_i_large_center.hbjson) | form | How does a large center opening illuminate a I-shaped plan? |
| [plan_i_offset_low](plan_i_offset_low.hbjson) | form | How does a offset low opening illuminate a I-shaped plan? |
| [plan_i_offset_high](plan_i_offset_high.hbjson) | form | How does a offset high opening illuminate a I-shaped plan? |
| [plan_i_triangle](plan_i_triangle.hbjson) | form | How does a triangle opening illuminate a I-shaped plan? |
| [plan_i_circle](plan_i_circle.hbjson) | form | How does a circle opening illuminate a I-shaped plan? |
| [plan_i_arch](plan_i_arch.hbjson) | form | How does a arch opening illuminate a I-shaped plan? |
| [plan_i_distributed](plan_i_distributed.hbjson) | form | How does a distributed opening illuminate a I-shaped plan? |
| [plan_j_small_center](plan_j_small_center.hbjson) | form | How does a small center opening illuminate a J-shaped plan? |
| [plan_j_large_center](plan_j_large_center.hbjson) | form | How does a large center opening illuminate a J-shaped plan? |
| [plan_j_offset_low](plan_j_offset_low.hbjson) | form | How does a offset low opening illuminate a J-shaped plan? |
| [plan_j_offset_high](plan_j_offset_high.hbjson) | form | How does a offset high opening illuminate a J-shaped plan? |
| [plan_j_triangle](plan_j_triangle.hbjson) | form | How does a triangle opening illuminate a J-shaped plan? |
| [plan_j_circle](plan_j_circle.hbjson) | form | How does a circle opening illuminate a J-shaped plan? |
| [plan_j_arch](plan_j_arch.hbjson) | form | How does a arch opening illuminate a J-shaped plan? |
| [plan_j_distributed](plan_j_distributed.hbjson) | form | How does a distributed opening illuminate a J-shaped plan? |
| [plan_l_small_center](plan_l_small_center.hbjson) | form | How does a small center opening illuminate a L-shaped plan? |
| [plan_l_large_center](plan_l_large_center.hbjson) | form | How does a large center opening illuminate a L-shaped plan? |
| [plan_l_offset_low](plan_l_offset_low.hbjson) | form | How does a offset low opening illuminate a L-shaped plan? |
| [plan_l_offset_high](plan_l_offset_high.hbjson) | form | How does a offset high opening illuminate a L-shaped plan? |
| [plan_l_triangle](plan_l_triangle.hbjson) | form | How does a triangle opening illuminate a L-shaped plan? |
| [plan_l_circle](plan_l_circle.hbjson) | form | How does a circle opening illuminate a L-shaped plan? |
| [plan_l_arch](plan_l_arch.hbjson) | form | How does a arch opening illuminate a L-shaped plan? |
| [plan_l_distributed](plan_l_distributed.hbjson) | form | How does a distributed opening illuminate a L-shaped plan? |
| [plan_t_small_center](plan_t_small_center.hbjson) | form | How does a small center opening illuminate a T-shaped plan? |
| [plan_t_large_center](plan_t_large_center.hbjson) | form | How does a large center opening illuminate a T-shaped plan? |
| [plan_t_offset_low](plan_t_offset_low.hbjson) | form | How does a offset low opening illuminate a T-shaped plan? |
| [plan_t_offset_high](plan_t_offset_high.hbjson) | form | How does a offset high opening illuminate a T-shaped plan? |
| [plan_t_triangle](plan_t_triangle.hbjson) | form | How does a triangle opening illuminate a T-shaped plan? |
| [plan_t_circle](plan_t_circle.hbjson) | form | How does a circle opening illuminate a T-shaped plan? |
| [plan_t_arch](plan_t_arch.hbjson) | form | How does a arch opening illuminate a T-shaped plan? |
| [plan_t_distributed](plan_t_distributed.hbjson) | form | How does a distributed opening illuminate a T-shaped plan? |
| [plan_cross_small_center](plan_cross_small_center.hbjson) | form | How does a small center opening illuminate a CROSS-shaped plan? |
| [plan_cross_large_center](plan_cross_large_center.hbjson) | form | How does a large center opening illuminate a CROSS-shaped plan? |
| [plan_cross_offset_low](plan_cross_offset_low.hbjson) | form | How does a offset low opening illuminate a CROSS-shaped plan? |
| [plan_cross_offset_high](plan_cross_offset_high.hbjson) | form | How does a offset high opening illuminate a CROSS-shaped plan? |
| [plan_cross_triangle](plan_cross_triangle.hbjson) | form | How does a triangle opening illuminate a CROSS-shaped plan? |
| [plan_cross_circle](plan_cross_circle.hbjson) | form | How does a circle opening illuminate a CROSS-shaped plan? |
| [plan_cross_arch](plan_cross_arch.hbjson) | form | How does a arch opening illuminate a CROSS-shaped plan? |
| [plan_cross_distributed](plan_cross_distributed.hbjson) | form | How does a distributed opening illuminate a CROSS-shaped plan? |
| [teaching_wwr20](teaching_wwr20.hbjson) | teaching | How does a 20% window-to-wall ratio light the base room? |
| [teaching_wwr40](teaching_wwr40.hbjson) | teaching | How does a 40% window-to-wall ratio light the base room? |
| [teaching_wwr60](teaching_wwr60.hbjson) | teaching | How does a 60% window-to-wall ratio light the base room? |
| [teaching_depth4](teaching_depth4.hbjson) | teaching | How does daylight fall off in a 4 m deep room? |
| [teaching_depth6](teaching_depth6.hbjson) | teaching | What is the 6 m deep teaching base room? |
| [teaching_depth8](teaching_depth8.hbjson) | teaching | How does daylight fall off in an 8 m deep room? |
| [teaching_depth10](teaching_depth10.hbjson) | teaching | How does daylight fall off in a 10 m deep room? |
| [teaching_reflectance30](teaching_reflectance30.hbjson) | teaching | How much does 0.3 surface reflectance cost at the back of the room? |
| [teaching_reflectance70](teaching_reflectance70.hbjson) | teaching | How much does 0.7 surface reflectance add at the back of the room? |
| [teaching_overhang050](teaching_overhang050.hbjson) | teaching | What does a 0.5 m overhang remove from the base room? |
| [teaching_overhang100](teaching_overhang100.hbjson) | teaching | What does a 1.0 m overhang remove from the base room? |
| [teaching_obstruction30](teaching_obstruction30.hbjson) | teaching | How does a 30 degree obstruction angle reduce sky access? |
| [teaching_obstruction60](teaching_obstruction60.hbjson) | teaching | How does a 60 degree obstruction angle reduce sky access? |
| [teaching_classroom](teaching_classroom.hbjson) | teaching | How is a 9 x 7 m classroom with three windows lit? |
| [teaching_office](teaching_office.hbjson) | teaching | How is a 12 x 8 m open-plan office with a ribbon window lit? |
| [teaching_living_room](teaching_living_room.hbjson) | teaching | How is a 5 x 4.5 m living room with a tall window lit? |

bl_info = {
    "name": "Utilities to set keyframes to linear interpolation",
    "blender": (2, 80, 0),
    "category": "Animation",
}

import bpy

class ANIM_OT_set_all_to_linear(bpy.types.Operator):
    bl_idname = "anim.set_all_to_linear"
    bl_label = "Set All Keyframes to Linear"
    bl_description = "Set all keyframes of the current action to linear interpolation"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.object and context.object.animation_data and context.object.animation_data.action:
            for fcurve in context.object.animation_data.action.fcurves:
                for keyframe in fcurve.keyframe_points:
                    keyframe.interpolation = 'LINEAR'
            self.report({'INFO'}, "All keyframes set to linear interpolation.")
        else:
            self.report({'WARNING'}, "No active action to modify.")
        return {'FINISHED'}

class ANIM_OT_set_selected_to_linear(bpy.types.Operator):
    bl_idname = "anim.set_selected_to_linear"
    bl_label = "Set Selected Keyframes to Linear"
    bl_description = "Set selected keyframes of the current action to linear interpolation"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.object and context.object.animation_data and context.object.animation_data.action:
            modified = False
            for fcurve in context.object.animation_data.action.fcurves:
                for keyframe in fcurve.keyframe_points:
                    if keyframe.select_control_point:  # Check if the keyframe is selected
                        keyframe.interpolation = 'LINEAR'
                        modified = True
            if modified:
                self.report({'INFO'}, "Selected keyframes set to linear interpolation.")
            else:
                self.report({'WARNING'}, "No keyframes selected.")
        else:
            self.report({'WARNING'}, "No active action to modify.")
        return {'FINISHED'}

def all_keyframes_to_linear_menu_func(self, context):
    self.layout.operator(ANIM_OT_set_all_to_linear.bl_idname)

def selected_keyframes_to_linear_menu_func(self, context):
    self.layout.operator(ANIM_OT_set_selected_to_linear.bl_idname)

def register():
    bpy.utils.register_class(ANIM_OT_set_all_to_linear)
    bpy.types.GRAPH_MT_key.append(all_keyframes_to_linear_menu_func)

    bpy.utils.register_class(ANIM_OT_set_selected_to_linear)
    bpy.types.GRAPH_MT_key.append(selected_keyframes_to_linear_menu_func)

def unregister():
    bpy.utils.unregister_class(ANIM_OT_set_all_to_linear)
    bpy.types.GRAPH_MT_key.remove(all_keyframes_to_linear_menu_func)

    bpy.utils.unregister_class(ANIM_OT_set_selected_to_linear)
    bpy.types.GRAPH_MT_key.remove(selected_keyframes_to_linear_menu_func)

if __name__ == "__main__":
    register()

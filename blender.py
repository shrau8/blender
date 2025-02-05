import bpy
import requests

SERVER_URL = "http://127.0.0.1:5000"

# Function to get transform data
def get_transform_data(obj):
    return {
        "position": [obj.location.x, obj.location.y, obj.location.z],
        "rotation": [obj.rotation_euler.x, obj.rotation_euler.y, obj.rotation_euler.z],
        "scale": [obj.scale.x, obj.scale.y, obj.scale.z]
    }

# Operator to send data
class SendTransformOperator(bpy.types.Operator):
    bl_idname = "object.send_transform"
    bl_label = "Send Transform"

    def execute(self, context):
        obj = bpy.context.active_object
        if obj:
            transform_data = get_transform_data(obj)
            response = requests.post(f"{SERVER_URL}/transform", json=transform_data)

            if response.status_code == 200:
                self.report({'INFO'}, "Transform data sent!")
            else:
                self.report({'ERROR'}, "Failed to send data")
        else:
            self.report({'ERROR'}, "No object selected")

        return {'FINISHED'}

# UI Panel
class TransformPanel(bpy.types.Panel):
    bl_label = "Transform Sync"
    bl_idname = "OBJECT_PT_transform_sync"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Transform Sync"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.send_transform")

# Register plugin
def register():
    bpy.utils.register_class(SendTransformOperator)
    bpy.utils.register_class(TransformPanel)

def unregister():
    bpy.utils.unregister_class(SendTransformOperator)
    bpy.utils.unregister_class(TransformPanel)

if __name__ == "__main__":
    register()

import bpy


# Main Panel
class IFC_PT_MainPanel(bpy.types.Panel):
    bl_label = "IFC Easy Render"
    bl_idname = "IFC_PT_MAINPANEL"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "IFC Easy Render"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Visualize and render IFC Models")


"""
    *******************************************************************
    Camera Setup Panel 
    *******************************************************************
"""


class IFC_PT_CameraSetup(bpy.types.Panel):
    bl_label = "Camera Setup"
    bl_idname = "IFC_PT_CAMERASETUP"
    bl_parent_id = "IFC_PT_MAINPANEL"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        layout.operator("camera.add_camera")


# Preset Camera Positions Subpanel
class IFC_PT_SubPanel_PresetPositions(bpy.types.Panel):
    bl_label = "Preset Camera Positions"
    bl_idname = "IFC_PT_SUBPANEL_PRESETPOSITIONS"
    bl_parent_id = "IFC_PT_CAMERASETUP"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, "camera_angle", text="Common Angles")
        layout.prop(context.scene, "saved_camera_angle", text="Saved Angles")
        layout.operator("camera.random_perspective", text="Random Perspective")


# Compositing Subpanel
class IFC_PT_SubPanel_Compositing(bpy.types.Panel):
    bl_label = "Compositing"
    bl_idname = "IFC_PT_SUBPANEL_COMPOSITING"
    bl_parent_id = "IFC_PT_CAMERASETUP"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, "camera_aspect_ratio", text="Aspect Ratio")


# Settings Subpanel
class IFC_PT_SubPanel_CameraSettings(bpy.types.Panel):
    bl_label = "Settings"
    bl_idname = "IFC_PT_SUBPANEL_CAMERASETTINGS"
    bl_parent_id = "IFC_PT_CAMERASETUP"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Positioning")
        layout.prop(context.scene, "camera_distance", text="Distance")
        layout.prop(context.scene, "camera_height_offset", text="Height Offset")
        layout.prop(context.scene, "camera_orbit_angle", text="Orbit Angle")
        layout.operator("camera.auto_frame", text="Auto-Frame")

        layout.label(text="Lens")
        layout.prop(context.scene, "camera_focal_length", text="Focal Length")
        layout.prop(context.scene, "camera_depth_of_field", text="Depth of Field")


# Saving Subpanel
class IFC_PT_SubPanel_CameraSaving(bpy.types.Panel):
    bl_label = "Saving"
    bl_idname = "IFC_PT_SUBPANEL_CAMERASAVING"
    bl_parent_id = "IFC_PT_CAMERASETUP"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, "camera_setup_name", text="Name")
        layout.operator("camera.save_setup", text="Save Current Setup")


# Operators
class CAMERA_OT_AddCamera(bpy.types.Operator):
    bl_label = "Add Camera"
    bl_idname = "camera.add_camera"

    def execute(self, context):
        return {"FINISHED"}


class CAMERA_OT_RandomPerspective(bpy.types.Operator):
    bl_label = "Random Perspective"
    bl_idname = "camera.random_perspective"

    def execute(self, context):
        return {"FINISHED"}


class CAMERA_OT_AutoFrame(bpy.types.Operator):
    bl_label = "Auto-Frame"
    bl_idname = "camera.auto_frame"

    def execute(self, context):
        return {"FINISHED"}


class CAMERA_OT_SaveSetup(bpy.types.Operator):
    bl_label = "Save Current Setup"
    bl_idname = "camera.save_setup"

    def execute(self, context):
        return {"FINISHED"}


#  Properties
def register_camera_properties():
    bpy.types.Scene.camera_angle = bpy.props.EnumProperty(
        name="Camera Angle",
        items=[
            ("TOP", "Top", ""),
            ("FRONT", "Front", ""),
            ("BACK", "Back", ""),
            ("LEFT", "Left", ""),
            ("RIGHT", "Right", ""),
            ("PERSPECTIVE", "Perspective", ""),
        ],
    )
    bpy.types.Scene.saved_camera_angle = bpy.props.EnumProperty(
        name="Saved Angles",
        items=[],
    )
    bpy.types.Scene.camera_distance = bpy.props.FloatProperty(
        name="Distance", default=10.0, min=1.0, max=100.0
    )
    bpy.types.Scene.camera_height_offset = bpy.props.FloatProperty(
        name="Height Offset", default=0.0, min=-10.0, max=10.0
    )
    bpy.types.Scene.camera_orbit_angle = bpy.props.FloatProperty(
        name="Orbit Angle", default=0.0, min=-180.0, max=180.0
    )
    bpy.types.Scene.camera_focal_length = bpy.props.FloatProperty(
        name="Focal Length", default=50.0, min=10.0, max=300.0
    )
    bpy.types.Scene.camera_depth_of_field = bpy.props.BoolProperty(
        name="Depth of Field", default=False
    )
    bpy.types.Scene.camera_setup_name = bpy.props.StringProperty(
        name="Setup Name", default=""
    )
    bpy.types.Scene.camera_aspect_ratio = bpy.props.EnumProperty(
        name="Aspect Ratio",
        items=[
            ("16:9", "16:9", ""),
            ("4:3", "4:3", ""),
            ("1:1", "1:1", ""),
            ("21:9", "21:9", ""),
        ],
        default="16:9",
    )


def unregister_camera_properties():
    del bpy.types.Scene.camera_aspect_ratio
    del bpy.types.Scene.camera_angle
    del bpy.types.Scene.saved_camera_angle
    del bpy.types.Scene.camera_distance
    del bpy.types.Scene.camera_height_offset
    del bpy.types.Scene.camera_orbit_angle
    del bpy.types.Scene.camera_focal_length
    del bpy.types.Scene.camera_depth_of_field
    del bpy.types.Scene.camera_setup_name


"""
    *******************************************************************
    Lighting Setup Panel 
    *******************************************************************
"""


class IFC_PT_LightingSetup(bpy.types.Panel):
    bl_label = "Lighting Setup"
    bl_idname = "IFC_PT_LIGHTINGSETUP"
    bl_parent_id = "IFC_PT_MAINPANEL"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "IFC Easy Render"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, "hdri_preset", text="HDRI Preset")
        layout.prop(context.scene, "hdri_intensity", text="Intensity")

        layout.label(text="Rotation:")
        row = layout.row()
        row.prop(context.scene, "hdri_rotation_x", text="X")
        row.prop(context.scene, "hdri_rotation_y", text="Y")
        row.prop(context.scene, "hdri_rotation_z", text="Z")


# Properties
def register_lighting_properties():
    bpy.types.Scene.hdri_intensity = bpy.props.FloatProperty(
        name="HDRI Intensity", default=1.0, min=0.1, max=5.0
    )

    bpy.types.Scene.hdri_rotation_x = bpy.props.FloatProperty(
        name="HDRI Rotation X", default=0.0, min=0.0, max=360.0
    )

    bpy.types.Scene.hdri_rotation_y = bpy.props.FloatProperty(
        name="HDRI Rotation Y", default=0.0, min=0.0, max=360.0
    )

    bpy.types.Scene.hdri_rotation_z = bpy.props.FloatProperty(
        name="HDRI Rotation Z", default=0.0, min=0.0, max=360.0
    )

    bpy.types.Scene.hdri_preset = bpy.props.EnumProperty(
        name="HDRI Selection",
        items=[
            ("SUNNY", "Sunny Day", ""),
            ("STUDIO", "Studio Light", ""),
            ("EVENING", "Evening Glow", ""),
        ],
    )


def unregister_lighting_properties():
    del bpy.types.Scene.hdri_intensity
    del bpy.types.Scene.hdri_rotation_x
    del bpy.types.Scene.hdri_rotation_y
    del bpy.types.Scene.hdri_rotation_z
    del bpy.types.Scene.hdri_preset


"""
    *******************************************************************
    Materials & Textures Panel 
    *******************************************************************
"""


class IFC_PT_MaterialsTextures(bpy.types.Panel):
    bl_label = "Materials & Textures"
    bl_idname = "IFC_PT_MATERIALS"
    bl_parent_id = "IFC_PT_MAINPANEL"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "IFC Easy Render"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        layout.prop(context.scene, "material_color", text="Color")

        layout.label(text="Material Properties")
        layout.operator("material.open_material_asset_library", text="Open Material Asset Library")
        layout.prop(context.scene, "material_roughness", text="Roughness")
        layout.prop(context.scene, "material_metallic", text="Metallic")


# Operators
class IFC_OT_OpenMaterialAssetLibrary(bpy.types.Operator):
    bl_idname = "material.open_material_asset_library"
    bl_label = "Open Material Asset Library"
    bl_description = "Open the Material Asset Library folder"

    def execute(self, context):
        pass
        return {"FINISHED"}


# Properties
def register_materials_properties():
    bpy.types.Scene.material_color = bpy.props.EnumProperty(
        name="Material Color",
        items=[
            ("RED", "Red", ""),
            ("GREEN", "Green", ""),
            ("BLUE", "Blue", ""),
            ("YELLOW", "Yellow", ""),
            ("WHITE", "White", ""),
            ("BLACK", "Black", ""),
        ],
    )
    bpy.types.Scene.material_roughness = bpy.props.FloatProperty(
        name="Roughness", default=0.0, min=0.0, max=1.0
    )
    bpy.types.Scene.material_metallic = bpy.props.FloatProperty(
        name="Metallic", default=0.0, min=0.0, max=1.0
    )


def unregister_materials_properties():
    del bpy.types.Scene.material_color
    del bpy.types.Scene.material_roughness
    del bpy.types.Scene.material_metallic


classes = [
    IFC_PT_MainPanel,
    # Camera
    IFC_PT_CameraSetup,
    IFC_PT_SubPanel_PresetPositions,
    IFC_PT_SubPanel_Compositing,
    IFC_PT_SubPanel_CameraSettings,
    IFC_PT_SubPanel_CameraSaving,
    CAMERA_OT_AddCamera,
    CAMERA_OT_RandomPerspective,
    CAMERA_OT_AutoFrame,
    CAMERA_OT_SaveSetup,
    # Lighting
    IFC_PT_LightingSetup,
    # Materials & Textures
    IFC_PT_MaterialsTextures,
    IFC_OT_OpenMaterialAssetLibrary,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    register_camera_properties()
    register_lighting_properties()
    register_materials_properties()


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    unregister_camera_properties()
    unregister_lighting_properties()
    unregister_materials_properties()


if __name__ == "__main__":
    register()

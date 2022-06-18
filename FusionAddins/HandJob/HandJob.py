# Author-
# Description-

import adsk.core, adsk.fusion, adsk.cam, traceback
import time
import math


def run(context):
    ui = None

    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        des = adsk.fusion.Design.cast(app.activeProduct)
        root = des.rootComponent
        
        # Components
        comp1 = root.occurrences.itemByName("index_finger v7:1")
        index_finger = comp1.component
        comp2 = root.occurrences.itemByName("middle_finger v18:1")
        middle_finger = comp2.component
        comp3 = root.occurrences.itemByName("ring_finger v7:1")
        ring_finger = comp3.component
        comp4 = root.occurrences.itemByName("little_finger v9:1")
        little_finger = comp4.component
        comp5 = root.occurrences.itemByName("thumb v4:1")
        thumb_finger = comp5.component

        joint1 = root.joints.itemByName("index_finger_rotation")
        joint2 = root.joints.itemByName("middle_finger_rotation")
        joint3 = root.joints.itemByName("ring_finger_rotation")
        joint4 = root.joints.itemByName("little_finger_rotation")
        joint5 = root.joints.itemByName("thumb_finger_rotation")

        # Find components joints
        occ1 = index_finger.joints.itemByName("index_core_joint")
        index_core = occ1.createForAssemblyContext(comp1)
        occ2 = middle_finger.joints.itemByName("middle_core_joint")
        middle_core = occ2.createForAssemblyContext(comp2)
        occ3 = ring_finger.joints.itemByName("ring_core_joint")
        ring_core = occ3.createForAssemblyContext(comp3)
        occ4 = little_finger.joints.itemByName("little_core_joint")
        little_core = occ4.createForAssemblyContext(comp4)
        occ5 = thumb_finger.joints.itemByName("thumb_core_joint")
        thumb_core = occ4.createForAssemblyContext(comp4)

        rev1 = adsk.fusion.RevoluteJointMotion.cast(joint1.jointMotion)
        rev2 = adsk.fusion.RevoluteJointMotion.cast(joint2.jointMotion)
        rev3 = adsk.fusion.RevoluteJointMotion.cast(joint3.jointMotion)
        rev4 = adsk.fusion.RevoluteJointMotion.cast(joint4.jointMotion)
        rev5 = adsk.fusion.RevoluteJointMotion.cast(joint5.jointMotion)
        
        rev5 = adsk.fusion.RevoluteJointMotion.cast(index_core.jointMotion)
        rev6 = adsk.fusion.RevoluteJointMotion.cast(middle_core.jointMotion)
        rev7 = adsk.fusion.RevoluteJointMotion.cast(ring_core.jointMotion)
        rev8 = adsk.fusion.RevoluteJointMotion.cast(little_core.jointMotion)
        rev9 = adsk.fusion.RevoluteJointMotion.cast(thumb_core.jointMotion)

        # Run only for one minute
        t_end = time.time() + 60 * 1
        while time.time() < t_end:
            with open(
                "C:\\Users\\marek\\AppData\\Roaming\\Autodesk\\Autodesk Fusion 360\\API\\Scripts\\HandJob\\coords.txt"
            ) as f:
                contents = f.read()
            coords = contents.split(".")
            # ui.messageBox(i)

            try:
                angle1 = int(coords[0]) * (math.pi / 180)
                angle2 = int(coords[1]) * (math.pi / 180)
                angle3 = int(coords[2]) * (math.pi / 180)
                angle4 = -1 * int(coords[3]) * (math.pi / 180)

                rev1.rotationValue = angle1
                rev2.rotationValue = angle2
                rev3.rotationValue = angle3
                rev4.rotationValue = angle4

                rev5.rotationValue = angle1
                rev6.rotationValue = angle2
                rev7.rotationValue = angle3
                rev8.rotationValue = -angle4

                adsk.doEvents()
            except:
                continue

            time.sleep(0.0001)

    except:
        if ui:
            ui.messageBox("Failed:\n{}".format(traceback.format_exc()))

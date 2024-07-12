# MadCap Flare Build Notification

A toast notification edited to fit as a MadCap Flare Build Notification.

## How to use

>**Important:** Python needs to be installed for this script to work in MadCap Flare. 

This script uses the module **win10toast**. To install:

1. Open your command prompt.
2. Type **pip install win10toast**.
3. Press **Enter**. 

After the install is complete, move on to the next section.

### Creating a Batch File

To implement the notification, users can run a batch file. Complete the steps in the next section to create a batch file that runs this notification.

1. Download the build notification python script.
2. Copy the path of the script.
3. Open a text-editor.

    >**Example:** Visual Studio Code, Notepad++, etc.

4. Type `@echo off` on one line, and `python` on the next line.

5. Paste the path of the python script in front of `python`.

```
@echo off
python C:path\to\python\file
```

6. Save and name the batch file.

### Running the Batch File in Flare

Once the batch file is complete, users can use it in MadCap Flare to run the build notification. 

1. Open a MadCap Flare project.
2. Open a Target.
3. Select the **Build Events** tab on the left hand menu of the target.
4. In the **Post-Build Event Command** section, copy and paste the location of the batch file.
    >**Example:** "D:\path\to\batch\file"
4. Save your changes.
5. Build the target.

After the build finishes, a notification should pop-up informing you that the build is complete. 


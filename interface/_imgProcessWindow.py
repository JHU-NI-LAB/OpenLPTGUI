import dearpygui.dearpygui as dpg

def showImgProcess(callbacks):
    with dpg.tab_bar():
        with dpg.tab(label='1. Create Image Files (Optional)'):
            showCreateImgFile(callbacks)
        with dpg.tab(label='2. Image Processing'):
            showActualImgProcess(callbacks)
        
    
def showCreateImgFile(callbacks):
    subwindow_width = dpg.get_item_width('imgProcess')
    subwindow_height = dpg.get_item_height('imgProcess')
    
    with dpg.group(horizontal=True):
        with dpg.child_window(width=0.3*subwindow_width, horizontal_scrollbar=True):
            with dpg.file_dialog(directory_selector=True, width=0.7*subwindow_width, height=0.9*subwindow_height, min_size=[400,300], file_count=20, show=False, tag='file_dialog_createImgfile', callback=callbacks.lptCreateImgFile.openFolder, cancel_callback=callbacks.lptCreateImgFile.cancelImportFolder):
                dpg.add_file_extension("", color=(150, 255, 150, 255))

            with dpg.group(horizontal=True):
                dpg.add_text('1. Select Image Main Folder')
                dpg.add_button(label='?', callback=callbacks.lptCreateImgFile.helpSelectFolder)
            dpg.add_button(label='Select', callback=lambda: dpg.show_item("file_dialog_createImgfile"))
            dpg.add_separator()
            
            dpg.add_text('2. Input Image Name Suffix')
            dpg.add_input_text(tag='lptImgNameSuffix', default_value='.tif', width=-1)
            dpg.add_separator()
            
            dpg.add_text('3. Save Image File Path')
            dpg.add_text('Input Frame Range')
            dpg.add_input_int(tag='lptImgFileFrameStart', default_value=0, min_value=0, width=-1, step=-1, label='Start')
            dpg.add_input_int(tag='lptImgFileFrameEnd', default_value=1000, min_value=0, width=-1, step=-1, label='End')
            dpg.add_file_dialog(directory_selector=True, width=0.7*subwindow_width, height=0.9*subwindow_height, min_size=[400,300], show=False, tag='lptImgFileOutputDialog', callback=callbacks.lptCreateImgFile.selectOutputFolder, cancel_callback=lambda: dpg.configure_item('lptImgFileOutputDialog', show=False))
            dpg.add_button(label='Select Output Folder', callback=lambda: dpg.show_item("lptImgFileOutputDialog"))
            dpg.add_button(label='Save', callback=callbacks.lptCreateImgFile.createImgFiles)
            dpg.add_separator()
            
            
            # error message
            with dpg.window(label="ERROR!", modal=True, show=False, tag="lptImgProcessCreate_noPath", no_title_bar=False):
                dpg.add_text("", tag="lptImgProcessCreate_noPathText")
                dpg.add_button(label="OK", width=-1, callback=lambda: dpg.configure_item("lptImgProcessCreate_noPath", show=False))
            
            # help window shown in the middle
            with dpg.window(label="Help!", modal=True, show=False, tag="lptImgProcessCreate_help", no_title_bar=False, width=0.3*subwindow_width, height=0.3*subwindow_height, pos=[0.35*subwindow_width,0.35*subwindow_height]):
                dpg.add_text("", tag="lptImgProcessCreate_helpText", wrap=0.295*subwindow_width)
                dpg.add_text("")
                dpg.add_separator()
                dpg.add_button(label="OK", width=-1, callback=lambda: dpg.configure_item("lptImgProcessCreate_help", show=False))
            
                  
        with dpg.child_window(horizontal_scrollbar=True):
            dpg.add_text('Imported Files:')
            with dpg.table(header_row=True, policy=dpg.mvTable_SizingFixedFit, row_background=True, resizable=True, no_host_extendX=False, hideable=True, borders_innerV=True, delay_search=True, borders_outerV=True, borders_innerH=True,
                borders_outerH=True, tag='lptCreateImgfileTable'):
                dpg.add_table_column(label='Cam Name', width_fixed=True)
                dpg.add_table_column(label='Folder Name', width_stretch=True)
                
            dpg.add_separator()
            dpg.add_text('Output Folder: --', tag='lptImgFileOutputFolder')
            dpg.add_text('Export Image File Status: --', tag='lptImgFileExportStatus')
                
    
    
def showActualImgProcess(callbacks):
    subwindow_width = dpg.get_item_width('imgProcess')
    subwindow_height = dpg.get_item_height('imgProcess')
    
    with dpg.group(horizontal=True):
        with dpg.child_window(width=0.3*subwindow_width, horizontal_scrollbar=True):
            with dpg.file_dialog(directory_selector=False, width=0.7*subwindow_width, height=0.9*subwindow_height, min_size=[400,300], file_count=100, show=False, tag='file_dialog_imgprocess', callback=callbacks.lptImgProcess.openImgFile, cancel_callback=callbacks.lptImgProcess.cancelImgImportFile):
                dpg.add_file_extension("", color=(150, 255, 150, 255))
                dpg.add_file_extension(".txt", color=(0, 255, 255, 255))

            with dpg.group(horizontal=True):
                dpg.add_text('1. Import Image Path Files')
                dpg.add_button(label='?', callback=callbacks.lptImgProcess.helpImportImgFile)
            dpg.add_button(label='Import Files', callback=lambda: dpg.show_item("file_dialog_imgprocess"))
            dpg.add_separator()
            
            dpg.add_text('2. Image Processing')
            dpg.add_text('Choose one camera to show sample image', tag='lptImgShowIDText')
            dpg.add_listbox(tag='lptImgShowID', callback=callbacks.lptImgProcess.importImg)
            dpg.add_input_int(label='Frame ID', tag='lptImgFrameID', default_value=0, min_value=0, max_value=1000000, callback=callbacks.lptImgProcess.importImg)

            with dpg.group(horizontal=True):
                dpg.add_checkbox(tag='lptInvertImgCheckbox', callback=lambda sender, app_data: callbacks.lptImgProcess.toggleAndExecuteQuery('invertImg', sender, app_data))
                dpg.add_text('Invert Image')
            dpg.add_separator()
            
            with dpg.group(horizontal=True):
                dpg.add_checkbox(tag='lptRemoveBkgCheckbox', callback=lambda sender, app_data: callbacks.lptImgProcess.toggleAndExecuteQuery('removeBkg', sender, app_data))
                dpg.add_text('Remove Background')
            dpg.add_text('Number of frames used for calculation')
            dpg.add_input_int(tag='lptRemoveBkgFrameNum', default_value=1000, min_value=1, max_value=10000, width=-1)
            dpg.add_text('Frame Step')
            dpg.add_input_int(tag='lptRemoveBkgFrameStep', default_value=20, min_value=1, max_value=1000, width=-1)
            dpg.add_button(label='Remove Background', callback=lambda: callbacks.lptImgProcess.executeQuery('removeBkg'))
            dpg.add_separator()
            
            with dpg.group(horizontal=True):
                dpg.add_checkbox(tag='lptBrightnessAndContrastCheckbox', callback=lambda sender, app_data: callbacks.lptImgProcess.toggleAndExecuteQuery('brightnessAndContrast', sender, app_data))
                dpg.add_text('Brightness and Contrast')
            dpg.add_text('Brightness')
            dpg.add_slider_int(default_value=0, min_value=-100, max_value=100, width=-1, tag='lptBrightnessSlider', callback=lambda: callbacks.lptImgProcess.executeQuery('brightnessAndContrast'))
            dpg.add_text('Contrast')
            dpg.add_slider_float(default_value=1.0, min_value=0.0, max_value=5.0, width=-1, tag='lptContrastSlider', callback=lambda: callbacks.lptImgProcess.executeQuery('brightnessAndContrast'))
            dpg.add_separator()
            
            with dpg.group(horizontal=True):
                dpg.add_checkbox(tag='lptImAdjustCheckbox', callback=lambda sender, app_data: callbacks.lptImgProcess.toggleAndExecuteQuery('imAdjust', sender, app_data))
                dpg.add_text('Image Adjust')
            dpg.add_text('Intensity Range')
            dpg.add_slider_int(tag='lptImAdjustRange', default_value=255, min_value=0, max_value=255, width=-1, callback=lambda: callbacks.lptImgProcess.executeQuery('imAdjust'))
            dpg.add_separator()
            
            with dpg.group(horizontal=True):
                dpg.add_checkbox(tag='lptLabvisionCheckbox', callback=lambda sender, app_data: callbacks.lptImgProcess.toggleAndExecuteQuery('labvision', sender, app_data))
                dpg.add_text('Sharpening Particle')
            dpg.add_text('Gaussian Smooth Std')
            dpg.add_slider_float(tag='lptGaussianBlurSlider', default_value=0.5, min_value=0, max_value=5, width=-1, callback=lambda: callbacks.lptImgProcess.executeQuery('labvision'))
            dpg.add_text('Mean Filter Size')
            dpg.add_slider_int(tag='lptFilterSizeSlider', default_value=100, min_value=1, max_value=1024, width=-1, callback=lambda: callbacks.lptImgProcess.executeQuery('labvision'))
            dpg.add_separator()
            
            dpg.add_text('3. Run Batch')
            dpg.add_file_dialog(directory_selector=True, width=0.7*subwindow_width, height=0.9*subwindow_height, min_size=[400,300], show=False, tag='lptImgOutputDialog', id="lptImgOutputDialog", callback=callbacks.lptImgProcess.selectFolder, cancel_callback=callbacks.lptImgProcess.cancelSelectFolder)
            dpg.add_button(label='Select Output Folder', callback=lambda: dpg.show_item("lptImgOutputDialog"))
            dpg.add_text('Output Folder: --', tag='lptImgOutputFolder')
            dpg.add_text('Input frame range to process: (start from 0)')
            dpg.add_input_int(tag='lptImgFrameRangeStart', default_value=0, min_value=0, width=-1, step=-1, label='Start')
            dpg.add_input_int(tag='lptImgFrameRangeEnd', default_value=1000, min_value=0, width=-1, step=-1, label='End')
            dpg.add_text('Input number of parallel threads:')
            dpg.add_input_int(tag='lptImgThreadNum', default_value=10, min_value=1, width=-1, step=-1)
            dpg.add_button(label='Run Batch', callback=callbacks.lptImgProcess.runBatch)       
            dpg.add_text('Status: --', tag='lptImgExportStatus')
            
            
            # error message 
            with dpg.window(label="ERROR!", modal=True, show=False, tag="noLptImgPath", no_title_bar=False):
                dpg.add_text("", tag="noLptImgPathText")
                dpg.add_button(label="OK", width=-1, callback=lambda: dpg.configure_item("noLptImgPath", show=False))
                
            
            # help window shown in the middle
            with dpg.window(label="Help!", modal=True, show=False, tag="lptImgProcess_help", no_title_bar=False, width=0.3*subwindow_width, height=0.3*subwindow_height, pos=[0.35*subwindow_width,0.35*subwindow_height]):
                dpg.add_text("", tag="lptImgProcess_helpText", wrap=0.295*subwindow_width)
                dpg.add_text("")
                dpg.add_separator()
                dpg.add_button(label="OK", width=-1, callback=lambda: dpg.configure_item("lptImgProcess_help", show=False))
        
        
        with dpg.child_window(horizontal_scrollbar=True):
            dpg.add_text('Imported Files:')
            with dpg.table(header_row=True, policy=dpg.mvTable_SizingFixedFit, row_background=True, resizable=True, no_host_extendX=False, hideable=True, borders_innerV=True, delay_search=True, borders_outerV=True, borders_innerH=True,
                borders_outerH=True, tag='lptImgFileTable'):
                dpg.add_table_column(label='Cam Name', width_fixed=True)
                dpg.add_table_column(label='File Name', width_fixed=True)
                dpg.add_table_column(label='Number of Frames', width_fixed=True)
                dpg.add_table_column(label='File Path', width_fixed=True)
            
            dpg.add_separator()
            dpg.add_text('Sample Image: --', tag='lptImgSampleName')
            dpg.add_text('(Height, Width) = (--, --)', tag='lptImgSampleSize')
            with dpg.plot(tag="lptImgPlotParent", label="LPT Image Processing", height=-1, width=-1):
                dpg.add_plot_legend()
                dpg.add_plot_axis(dpg.mvXAxis, label="x", tag="lptImgProcess_x_axis")
                dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="lptImgProcess_y_axis", invert=True)

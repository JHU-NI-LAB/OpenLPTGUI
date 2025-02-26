import dearpygui.dearpygui as dpg

def showFiltering(callbacks):
    subwindow_width = dpg.get_item_width('calibPlate')
    subwindow_height = dpg.get_item_height('calibPlate')    
    
    with dpg.group(horizontal=True):
        with dpg.child_window(width=0.3*subwindow_width):
            # with dpg.group(horizontal=True):
            #     dpg.add_checkbox(tag='invertImageCheckbox', callback=lambda sender, app_data: callbacks.imageProcessing.toggleAndExecuteQuery('invertImage', sender, app_data))
            #     dpg.add_text('Invert Image')
            # dpg.add_separator()
            
            with dpg.group(horizontal=True):
                dpg.add_checkbox(tag='setAreaColorCheckbox', callback=lambda sender, app_data: callbacks.imageProcessing.toggleAndExecuteQuery('setAreaColor', sender, app_data))
                dpg.add_text('Remove Area')
                dpg.add_button(label='?', callback=callbacks.imageProcessing.helpMaskArea)
            # dpg.add_color_picker(tag='areaColorPicker', default_value=[255, 255, 255, 255], width=-1)
            dpg.add_listbox(tag='areaColorPicker', items=['White', 'Black'], default_value='Black', width=-1, num_items=2)
            dpg.add_button(tag='setAreaColorButton', width=-1, label='Apply Method', callback=lambda sender, app_data: callbacks.imageProcessing.executeQuery('setAreaColor'))
            dpg.add_separator()
            
            with dpg.group(horizontal=True):
                dpg.add_checkbox(tag='histogramCheckbox', callback=lambda sender, app_data: callbacks.imageProcessing.toggleAndExecuteQuery('histogramEqualization', sender, app_data))
                dpg.add_text('Histogram Equalization')
            dpg.add_separator()

            with dpg.group(horizontal=True):
                dpg.add_checkbox(tag='brightnessAndContrastCheckbox', callback=lambda sender, app_data: callbacks.imageProcessing.toggleAndExecuteQuery('brightnessAndContrast', sender, app_data))
                dpg.add_text('Brightness and Contrast')
            dpg.add_text('Brightness')
            dpg.add_slider_int(default_value=0, min_value=-100, max_value=100, width=-1, tag='brightnessSlider', callback=lambda: callbacks.imageProcessing.executeQuery('brightnessAndContrast'))
            dpg.add_text('Contrast')
            dpg.add_slider_float(default_value=1.0, min_value=0.0, max_value=3.0, width=-1, tag='contrastSlider', callback=lambda: callbacks.imageProcessing.executeQuery('brightnessAndContrast'))
            dpg.add_separator()
            
            with dpg.group(horizontal=True):
                dpg.add_text('Remove Noise Section')
                dpg.add_button(label='?', callback=callbacks.imageProcessing.helpRemoveNoise)
            
            with dpg.group(horizontal=True):
                dpg.add_checkbox(tag='averageBlurCheckbox', callback=lambda sender, app_data: callbacks.imageProcessing.toggleAndExecuteQuery('averageBlur', sender, app_data))
                dpg.add_text('Average Blur')
            dpg.add_text('Kernel Size')
            dpg.add_slider_int(tag='averageBlurSlider', default_value=1, min_value=1, max_value=100, width=-1, callback=lambda: callbacks.imageProcessing.executeQuery('averageBlur'))
            # dpg.add_separator()

            with dpg.group(horizontal=True):
                dpg.add_checkbox(tag='gaussianBlurCheckbox', callback=lambda sender, app_data: callbacks.imageProcessing.toggleAndExecuteQuery('gaussianBlur', sender, app_data))
                dpg.add_text('Gaussian Blur')
            dpg.add_text('Kernel Size')
            dpg.add_slider_float(tag='gaussianBlurSlider', default_value=0.5, min_value=0, max_value=10, width=-1, callback=lambda: callbacks.imageProcessing.executeQuery('gaussianBlur'))
            # dpg.add_separator()

            with dpg.group(horizontal=True):
                dpg.add_checkbox(tag='medianBlurCheckbox', callback=lambda sender, app_data: callbacks.imageProcessing.toggleAndExecuteQuery('medianBlur', sender, app_data))
                dpg.add_text('Median Blur')
            dpg.add_text('Kernel Size')
            dpg.add_slider_int(tag='medianBlurSlider', default_value=1, min_value=1, max_value=100, width=-1, callback=lambda: callbacks.imageProcessing.executeQuery('medianBlur'))
            dpg.add_separator()
                
            with dpg.group(tag="exportImageAsFileFilteringGroup", show=False):
                dpg.add_text("Save Image")
                dpg.add_button(tag='exportImageAsFileFiltering', width=-1, label='Export Image as File', callback=lambda sender, app_data: callbacks.imageProcessing.exportImage(sender, app_data, 'Filtering'))
                dpg.add_separator()
            
            # help window 
            with dpg.window(label="Help!", modal=True, show=False, tag="filteringTab_help", no_title_bar=False, pos=[0.35*subwindow_width,0.35*subwindow_height], width=0.3*subwindow_width, height=0.3*subwindow_height):
                dpg.add_text("", tag="filteringTab_helpText", wrap=0.295*subwindow_width)
                dpg.add_text("")
                dpg.add_separator()
                dpg.add_button(label="OK", width=-1, callback=lambda: dpg.configure_item("filteringTab_help", show=False))
            

            
        with dpg.child_window(tag='FilteringParent'):
            with dpg.plot(tag="FilteringPlotParent", label="Filtering", height=-1, width=-1, query=True, query_button=dpg.mvMouseButton_Left, pan_button=dpg.mvMouseButton_Middle):
                dpg.add_plot_legend()
                dpg.add_plot_axis(dpg.mvXAxis, label="x", tag="Filtering_x_axis")
                dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="Filtering_y_axis", invert=True)
                            
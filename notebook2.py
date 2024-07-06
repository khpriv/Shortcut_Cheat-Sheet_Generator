import dearpygui.dearpygui as dpg

dpg.create_context()

dpg.push_container_stack(dpg.add_window(label="Tutorial"))

dpg.push_container_stack(dpg.add_menu_bar())

dpg.push_container_stack(dpg.add_menu(label="Themes"))
dpg.add_menu_item(label="Dark")
dpg.add_menu_item(label="Light")
dpg.pop_container_stack()

# remove menu_bar from container stack
dpg.pop_container_stack()

# remove window from container stack
dpg.pop_container_stack()

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
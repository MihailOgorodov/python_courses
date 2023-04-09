import model
import text_fields as txt
import view


def start_pb():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.load_file()
                view.print_info(txt.load_successful)
            case 2:
                model.safe_file()
                view.print_info(txt.save_successful)
            case 3:
                pb = model.get_pb()
                view.show_contacts(pb, txt.no_contact_or_file)
            case 4:
                contact = view.new_contact()
                model.add_contact(contact)
                view.print_info(txt.new_contact_successful)
            case 5:
                word = view.input_word()
                result = model.find_contact(word)
                view.show_contacts(result, txt.search_contact_false)
            case 6:
                pb = model.get_pb()
                view.show_contacts(pb, txt.no_contact_or_file)
                edited_contact = view.edit_contact(pb, txt.input_index)
                model.edit_contact(edited_contact)
                view.print_info(txt.contact_successful_edited)
            case 7:
                pb = model.get_pb()
                view.show_contacts(pb, txt.no_contact_or_file)
                index = view.input_index(pb, txt.input_delete_index)
                view.print_info(txt.delete_contact(model.delete_contact(index)))
            case 8:
                if model.exit_pb():
                    if view.confirm(txt.is_changed):
                        model.safe_file()
                view.print_info(txt.exit)
                exit()

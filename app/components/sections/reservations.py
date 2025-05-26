import reflex as rx
from app.states.state import GlobalState


def reservation_form_field(
    label: str,
    name: str,
    placeholder: str = "",
    type: str = "text",
    is_textarea: bool = False,
    value: rx.Var | str = "",
) -> rx.Component:
    input_props = {
        "name": name,
        "placeholder": placeholder,
        "type": type,
        "default_value": value,
        "on_change": lambda val: rx.cond(
            type != "number",
            GlobalState.handle_reservation_form_change(
                name, val
            ),
            GlobalState.handle_reservation_form_change(
                name, val
            ),
        ),
        "class_name": "w-full p-3 border border-stone-300 rounded-lg focus:ring-2 focus:ring-amber-500 focus:border-amber-500 transition-colors bg-white text-stone-700 placeholder-stone-400",
    }
    if is_textarea:
        return rx.el.div(
            rx.el.label(
                label,
                class_name="block text-sm font-medium text-stone-700 mb-1",
            ),
            rx.el.textarea(**input_props, rows=4),
            class_name="mb-4",
        )
    return rx.el.div(
        rx.el.label(
            label,
            class_name="block text-sm font-medium text-stone-700 mb-1",
        ),
        rx.el.input(**input_props),
        class_name="mb-4",
    )


def reservations_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Réservez Votre Événement",
                class_name="text-3xl md:text-4xl font-bold text-stone-800 mb-8 text-center",
            ),
            rx.cond(
                GlobalState.show_reservation_confirmation,
                rx.el.div(
                    rx.el.h3(
                        "Merci pour votre réservation !",
                        class_name="text-2xl font-semibold text-green-600 mb-3",
                    ),
                    rx.el.p(
                        "Nous avons bien reçu votre demande et vous contacterons sous peu pour confirmer les détails.",
                        class_name="text-stone-700 mb-4",
                    ),
                    rx.el.button(
                        "Nouvelle Réservation",
                        on_click=GlobalState.close_reservation_confirmation,
                        class_name="bg-amber-500 hover:bg-amber-600 text-stone-800 font-semibold py-2 px-4 rounded-lg transition-colors",
                    ),
                    class_name="bg-green-50 border border-green-200 p-6 rounded-lg text-center shadow-md",
                ),
                rx.el.form(
                    rx.el.div(
                        reservation_form_field(
                            label="Type d'événement",
                            name="event_type",
                            placeholder="Ex: Anniversaire, Mariage, Réunion d'entreprise",
                            value=GlobalState.reservation_form_data[
                                "event_type"
                            ],
                        ),
                        reservation_form_field(
                            label="Nombre de convives (environ)",
                            name="num_guests",
                            type="number",
                            placeholder="Ex: 50",
                            value=GlobalState.reservation_form_data[
                                "num_guests"
                            ].to_string(),
                        ),
                        reservation_form_field(
                            label="Date de l'événement",
                            name="date",
                            type="date",
                            value=GlobalState.reservation_form_data[
                                "date"
                            ],
                        ),
                        reservation_form_field(
                            label="Votre Nom Complet",
                            name="name",
                            placeholder="Jean Dupont",
                            value=GlobalState.reservation_form_data[
                                "name"
                            ],
                        ),
                        reservation_form_field(
                            label="Votre Email",
                            name="email",
                            type="email",
                            placeholder="jean.dupont@example.com",
                            value=GlobalState.reservation_form_data[
                                "email"
                            ],
                        ),
                        reservation_form_field(
                            label="Votre Téléphone",
                            name="phone",
                            type="tel",
                            placeholder="0612345678",
                            value=GlobalState.reservation_form_data[
                                "phone"
                            ],
                        ),
                        rx.el.button(
                            "Envoyer la Demande",
                            type="submit",
                            class_name="w-full bg-amber-500 hover:bg-amber-600 text-stone-800 font-semibold py-3 px-6 rounded-lg text-lg transition-colors shadow-md hover:shadow-lg",
                        ),
                        class_name="grid grid-cols-1 md:grid-cols-2 gap-x-6 gap-y-0",
                    ),
                    on_submit=GlobalState.handle_reservation_submit,
                    reset_on_submit=False,
                    class_name="max-w-3xl mx-auto p-8 bg-white rounded-xl shadow-xl border border-amber-200",
                ),
            ),
            class_name="max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:px-8",
        ),
        class_name="bg-white",
        id="reservations",
    )
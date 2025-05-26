import reflex as rx
from app.states.state import GlobalState


def contact_form_field(
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
        "on_change": lambda val: GlobalState.handle_contact_form_change(
            name, val
        ),
        "class_name": "w-full p-3 border border-stone-300 rounded-lg focus:ring-2 focus:ring-amber-500 focus:border-amber-500 transition-colors bg-white text-stone-700 placeholder-stone-400",
    }
    if is_textarea:
        return rx.el.div(
            rx.el.label(
                label,
                class_name="block text-sm font-medium text-stone-700 mb-1",
            ),
            rx.el.textarea(**input_props, rows=5),
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


def contact_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Contactez-Nous",
                class_name="text-3xl md:text-4xl font-bold text-stone-800 mb-12 text-center",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Envoyez-nous un message",
                        class_name="text-2xl font-semibold text-stone-800 mb-6",
                    ),
                    rx.cond(
                        GlobalState.show_contact_confirmation,
                        rx.el.div(
                            rx.el.h3(
                                "Message envoyé !",
                                class_name="text-xl font-semibold text-green-600 mb-2",
                            ),
                            rx.el.p(
                                "Merci de nous avoir contactés. Nous reviendrons vers vous rapidement.",
                                class_name="text-stone-700 mb-3",
                            ),
                            rx.el.button(
                                "Nouveau Message",
                                on_click=GlobalState.close_contact_confirmation,
                                class_name="bg-amber-500 hover:bg-amber-600 text-stone-800 font-semibold py-2 px-3 rounded-lg transition-colors text-sm",
                            ),
                            class_name="bg-green-50 border border-green-200 p-4 rounded-lg text-center shadow-sm mb-6",
                        ),
                        rx.el.form(
                            contact_form_field(
                                label="Votre Nom",
                                name="name",
                                placeholder="Alice Martin",
                                value=GlobalState.contact_form_data[
                                    "name"
                                ],
                            ),
                            contact_form_field(
                                label="Votre Email",
                                name="email",
                                type="email",
                                placeholder="alice.martin@example.com",
                                value=GlobalState.contact_form_data[
                                    "email"
                                ],
                            ),
                            contact_form_field(
                                label="Votre Message",
                                name="message",
                                placeholder="Écrivez votre message ici...",
                                is_textarea=True,
                                value=GlobalState.contact_form_data[
                                    "message"
                                ],
                            ),
                            rx.el.button(
                                "Envoyer",
                                type="submit",
                                class_name="w-full bg-amber-500 hover:bg-amber-600 text-stone-800 font-semibold py-3 px-6 rounded-lg text-lg transition-colors shadow-md hover:shadow-lg",
                            ),
                            on_submit=GlobalState.handle_contact_submit,
                            reset_on_submit=False,
                            class_name="space-y-0",
                        ),
                    ),
                    class_name="w-full lg:w-1/2 p-8 bg-white rounded-xl shadow-xl border border-amber-200",
                ),
                rx.el.div(
                    rx.el.h3(
                        "Nos Coordonnées & Plan",
                        class_name="text-2xl font-semibold text-stone-800 mb-6",
                    ),
                    rx.el.div(
                        rx.el.p(
                            rx.icon(
                                tag="mail",
                                class_name="inline mr-2 text-amber-600",
                            ),
                            GlobalState.contact_email,
                            class_name="text-stone-700 mb-2",
                        ),
                        rx.el.p(
                            rx.icon(
                                tag="phone",
                                class_name="inline mr-2 text-amber-600",
                            ),
                            GlobalState.contact_phone,
                            class_name="text-stone-700 mb-2",
                        ),
                        rx.el.p(
                            rx.icon(
                                tag="map-pin",
                                class_name="inline mr-2 text-amber-600",
                            ),
                            GlobalState.address,
                            class_name="text-stone-700 mb-6",
                        ),
                    ),
                    rx.el.iframe(
                        src=GlobalState.google_maps_embed_url,
                        width="100%",
                        height="300",
                        style={"border": "0"},
                        allow_fullscreen="",
                        loading="lazy",
                        referrer_policy="no-referrer-when-downgrade",
                        class_name="rounded-lg shadow-md",
                    ),
                    class_name="w-full lg:w-1/2 p-8",
                ),
                class_name="flex flex-col lg:flex-row gap-12",
            ),
            class_name="max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:px-8",
        ),
        class_name="bg-amber-50",
        id="contact",
    )
import os
from pathlib import Path

import modal
from fasthtml import common as fh
from starlette.middleware.cors import CORSMiddleware

# -----------------------------------------------------------------------------

NAME = "engr110"
PARENT_PATH = Path(__file__).parent


def get_app():  # noqa: C901
    # setup
    def _not_found(req, exc):
        message = "Page not found!"
        typing_steps = len(message)
        return (
            fh.Title(NAME + " | 404"),
            fh.Div(
                nav(),
                fh.Main(
                    fh.Div(
                        fh.P(
                            message,
                            hx_indicator="#spinner",
                            cls="text-2xl text-red-300 animate-typing overflow-hidden whitespace-nowrap border-r-4 border-red-300",
                            style=f"animation: typing 2s steps({typing_steps}, end), blink-caret .75s step-end infinite",
                        ),
                    ),  # to contain typing animation
                    cls="flex flex-col justify-center items-center grow gap-4 p-8",
                ),
                toast_container(),
                footer(),
                cls="flex flex-col justify-between min-h-screen text-slate-100 bg-zinc-900 w-full",
            ),
        )

    f_app, _ = fh.fast_app(
        ws_hdr=True,
        exception_handlers={404: _not_found},
        hdrs=[
            fh.Script(src="https://cdn.tailwindcss.com"),
            fh.HighlightJS(langs=["python", "javascript", "html", "css"]),
            fh.Link(rel="icon", href="/favicon.ico", type="image/x-icon"),
            fh.Style(
                """
                @keyframes typing {
                from { width: 0; }
                to { width: 100%; }
                }
                @keyframes blink-caret {
                    from, to { border-color: transparent; }
                    50% { border-color: red; }
                }
                .htmx-swapping {
                    opacity: 0;
                    transition: opacity .25s ease-out;
                }
                """
            ),
        ],
        live=os.getenv("LIVE", False),
        debug=os.getenv("DEBUG", False),
        boost=True,
    )
    fh.setup_toasts(f_app)
    f_app.add_middleware(
        CORSMiddleware,
        allow_origins=["/"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    page_cls = (
        "flex flex-col justify-between min-h-screen w-full bg-zinc-900 text-slate-100 font-mono font-family:Consolas, Monaco, 'Lucida Console', 'Liberation Mono', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Courier New'",
    )
    link_cls = "text-blue-300 hover:text-blue-100"

    ## layout
    def nav():
        return fh.Nav(
            fh.A("home", href="/", cls="text-xl " + link_cls),
            fh.Svg(
                fh.NotStr(
                    """<style>
                    .spinner_zWVm { animation: spinner_5QiW 1.2s linear infinite, spinner_PnZo 1.2s linear infinite; }
                    .spinner_gfyD { animation: spinner_5QiW 1.2s linear infinite, spinner_4j7o 1.2s linear infinite; animation-delay: .1s; }
                    .spinner_T5JJ { animation: spinner_5QiW 1.2s linear infinite, spinner_fLK4 1.2s linear infinite; animation-delay: .1s; }
                    .spinner_E3Wz { animation: spinner_5QiW 1.2s linear infinite, spinner_tDji 1.2s linear infinite; animation-delay: .2s; }
                    .spinner_g2vs { animation: spinner_5QiW 1.2s linear infinite, spinner_CMiT 1.2s linear infinite; animation-delay: .2s; }
                    .spinner_ctYB { animation: spinner_5QiW 1.2s linear infinite, spinner_cHKR 1.2s linear infinite; animation-delay: .2s; }
                    .spinner_BDNj { animation: spinner_5QiW 1.2s linear infinite, spinner_Re6e 1.2s linear infinite; animation-delay: .3s; }
                    .spinner_rCw3 { animation: spinner_5QiW 1.2s linear infinite, spinner_EJmJ 1.2s linear infinite; animation-delay: .3s; }
                    .spinner_Rszm { animation: spinner_5QiW 1.2s linear infinite, spinner_YJOP 1.2s linear infinite; animation-delay: .4s; }
                    @keyframes spinner_5QiW { 0%, 50% { width: 7.33px; height: 7.33px; } 25% { width: 1.33px; height: 1.33px; } }
                    @keyframes spinner_PnZo { 0%, 50% { x: 1px; y: 1px; } 25% { x: 4px; y: 4px; } }
                    @keyframes spinner_4j7o { 0%, 50% { x: 8.33px; y: 1px; } 25% { x: 11.33px; y: 4px; } }
                    @keyframes spinner_fLK4 { 0%, 50% { x: 1px; y: 8.33px; } 25% { x: 4px; y: 11.33px; } }
                    @keyframes spinner_tDji { 0%, 50% { x: 15.66px; y: 1px; } 25% { x: 18.66px; y: 4px; } }
                    @keyframes spinner_CMiT { 0%, 50% { x: 8.33px; y: 8.33px; } 25% { x: 11.33px; y: 11.33px; } }
                    @keyframes spinner_cHKR { 0%, 50% { x: 1px; y: 15.66px; } 25% { x: 4px; y: 18.66px; } }
                    @keyframes spinner_Re6e { 0%, 50% { x: 15.66px; y: 8.33px; } 25% { x: 18.66px; y: 11.33px; } }
                    @keyframes spinner_EJmJ { 0%, 50% { x: 8.33px; y: 15.66px; } 25% { x: 11.33px; y: 18.66px; } }
                    @keyframes spinner_YJOP { 0%, 50% { x: 15.66px; y: 15.66px; } 25% { x: 18.66px; y: 18.66px; } }
                </style>
                <rect class="spinner_zWVm" x="1" y="1" width="7.33" height="7.33"/>
                <rect class="spinner_gfyD" x="8.33" y="1" width="7.33" height="7.33"/>
                <rect class="spinner_T5JJ" x="1" y="8.33" width="7.33" height="7.33"/>
                <rect class="spinner_E3Wz" x="15.66" y="1" width="7.33" height="7.33"/>
                <rect class="spinner_g2vs" x="8.33" y="8.33" width="7.33" height="7.33"/>
                <rect class="spinner_ctYB" x="1" y="15.66" width="7.33" height="7.33"/>
                <rect class="spinner_BDNj" x="15.66" y="8.33" width="7.33" height="7.33"/>
                <rect class="spinner_rCw3" x="8.33" y="15.66" width="7.33" height="7.33"/>
                <rect class="spinner_Rszm" x="15.66" y="15.66" width="7.33" height="7.33"/>
                """
                ),
                id="spinner",
                cls="htmx-indicator w-8 h-8 absolute top-12 md:top-6 left-1/2 transform -translate-x-1/2 fill-blue-300",
            ),
            fh.Div(
                fh.A(
                    "about me",
                    href="/about-me",
                    cls="text-lg " + link_cls,
                ),
                fh.A(
                    "project",
                    href="/project",
                    cls="text-lg " + link_cls,
                ),
                cls="flex items-center gap-4 md:gap-8",
            ),
            cls="flex justify-between items-center p-4 relative",
        )

    def main_content(
        session,
    ):
        return fh.Main(
            fh.Div(
                fh.P(
                    "Hi, I'm Andrew.",
                ),
                fh.P(
                    "This is my website for SCU's ENGR 110 class.",
                ),
                fh.P("Check out the links above for more."),
                cls="w-full md:w-2/3 flex flex-col gap-4 justify-center items-center",
            ),
            cls="flex flex-col justify-center items-center grow gap-4 p-8",
        )

    def about_content(
        session,
    ):
        return fh.Main(
            fh.Div(
                fh.P(
                    "I'm a 3rd year CSEN student at SCU.",
                ),
                fh.Img(
                    src="/profile.jpeg",
                    alt="Profile Picture",
                    cls="max-h-60 max-w-60 object-contain",
                ),
                cls="w-full md:w-2/3 flex flex-col gap-4 justify-center items-center",
            ),
            cls="flex flex-col justify-center items-center grow gap-4 p-8",
        )

    def project_content(session):
        return fh.Main(
            fh.Div(
                fh.P(
                    "1/14/25",
                ),
                fh.P(
                    "This is my first choice partner because I really enjoy working on AI, especially when applied to healthcare.",
                ),
                fh.Img(src="/hw1.png", cls="object-contain"),
                # TODO: fh.Embed(src="/hw1.pdf", type="application/pdf", width="100%", height="500px"),
                cls="w-full md:w-2/3 flex flex-col gap-4 justify-center items-center",
            ),
            cls="flex flex-col justify-center items-center grow gap-4 p-8",
        )

    def toast_container():
        return fh.Div(id="toast-container", cls="hidden")

    def footer():
        return fh.Footer(
            fh.Div(
                fh.P("Made by"),
                fh.A(
                    "Andrew Hinh",
                    href="https://andrewhinh.github.io/",
                    cls="font-bold " + link_cls,
                ),
                cls="flex flex-col text-right gap-0.5",
            ),
            cls="flex justify-end items-center p-4 text-sm md:text-lg",
        )

    # routes
    ## for images, CSS, etc.
    @f_app.get("/{fname:path}.{ext:static}")
    def static_files(fname: str, ext: str):
        static_file_path = PARENT_PATH / f"{fname}.{ext}"
        if static_file_path.exists():
            return fh.FileResponse(static_file_path)

    ## toasts without target
    @f_app.post("/toast")
    def toast(session, message: str, type: str):
        fh.add_toast(session, message, type)
        return toast_container()

    ## pages
    @f_app.get("/")
    def home(
        session,
    ):
        return (
            fh.Title(NAME),
            fh.Div(
                nav(),
                main_content(session),
                toast_container(),
                footer(),
                cls=page_cls,
            ),
            fh.Script(
                """
                document.addEventListener('htmx:beforeRequest', (event) => {
                    if (event.target.id === 'export-gens-csv') {
                        event.preventDefault();
                        window.location.href = "/export-gens";
                    }
                });
            """
            ),
        )

    @f_app.get("/about-me")
    def about_me(
        session,
    ):
        return (
            fh.Title(NAME + " | " + "about me"),
            fh.Div(
                nav(),
                about_content(session),
                toast_container(),
                footer(),
                cls=page_cls,
            ),
        )

    @f_app.get("/project")
    def project(
        session,
    ):
        return (
            fh.Title(NAME + " | " + "project"),
            fh.Div(
                nav(),
                project_content(session),
                toast_container(),
                footer(),
                cls=page_cls,
            ),
        )

    return f_app


f_app = get_app()

# -----------------------------------------------------------------------------

# Modal
PYTHON_VERSION = "3.12"
IMAGE = (
    modal.Image.debian_slim(python_version=PYTHON_VERSION)
    .pip_install(  # add Python dependencies
        "python-fasthtml==0.6.10",
        "sqlite-minutils==4.0.3",  # needed for fasthtml
    )
    .copy_local_dir(PARENT_PATH / "assets", "/root")
)
MINUTES = 60  # seconds
FE_TIMEOUT = 5 * MINUTES
FE_CONTAINER_IDLE_TIMEOUT = 15 * MINUTES
FE_ALLOW_CONCURRENT_INPUTS = 1000  # max

APP_NAME = f"{NAME}-frontend"
app = modal.App(APP_NAME)

# -----------------------------------------------------------------------------


@app.function(
    image=IMAGE,
    timeout=FE_TIMEOUT,
    container_idle_timeout=FE_CONTAINER_IDLE_TIMEOUT,
    allow_concurrent_inputs=FE_ALLOW_CONCURRENT_INPUTS,
)
@modal.asgi_app()
def modal_get():
    return f_app


if __name__ == "__main__":
    fh.serve(app="f_app")
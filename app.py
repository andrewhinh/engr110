import os
from pathlib import Path

import modal
from fasthtml import common as fh
from simpleicons.icons import si_github
from starlette.middleware.cors import CORSMiddleware

# -----------------------------------------------------------------------------

NAME = "engr110"
PARENT_PATH = Path(__file__).parent


def get_app():  # noqa: C901
    # setup
    page_cls = (
        "flex flex-col justify-between min-h-screen w-full bg-zinc-900 text-slate-50 font-mono font-family:Consolas, Monaco, 'Lucida Console', 'Liberation Mono', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Courier New'",
    )
    main_ctnr_cls = "flex flex-col justify-center items-center grow gap-10 p-8"
    page_ctnt_cls = "w-full flex flex-col items-center gap-8"
    link_cls = "text-blue-300 hover:text-blue-100"

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
                    cls=main_ctnr_cls,
                ),
                toast_container(),
                footer(),
                cls=page_cls,
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

    ## layout
    def nav():
        return fh.Nav(
            fh.A("home", href="/", cls="text-lg " + link_cls),
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
                cls="htmx-indicator w-8 h-8 absolute top-16 md:top-6 left-1/2 transform -translate-x-1/2 fill-blue-300",
            ),
            fh.Div(
                fh.A(
                    "about us",
                    href="/about-us",
                    cls="text-lg " + link_cls,
                ),
                fh.A(
                    "partner",
                    href="/partner",
                    cls="text-lg " + link_cls,
                ),
                fh.A(
                    "blog",
                    href="/blog",
                    cls="text-lg " + link_cls,
                ),
                cls="text-right md:text-left grid grid-cols-2 justify-items-end md:flex gap-4 md:gap-8",
                style="direction: rtl;",
            ),
            cls="flex justify-between p-4 relative",
        )

    def home_content():
        return fh.Main(
            fh.Div(
                fh.P("MHF Annotated Labeling Project", cls="text-4xl text-center"),
                cls="md:w-2/3 justify-center " + page_ctnt_cls,
            ),
            fh.Div(
                fh.P(
                    "This website contains information for the SCU ENGR 110 Winter 2025 ",
                    fh.B(fh.U("MHF Annotated Labeling Project")),
                    ".",
                ),
                fh.Img(
                    src="/assets/example.png",
                    alt="Example ultrasound",
                    hx_indicator="#spinner",
                    hx_trigger="load",
                    cls="w-full object-contain",
                ),
                fh.P("Check out the links above in the navigation bar for more."),
                cls="md:w-1/3 justify-center " + page_ctnt_cls,
            ),
            hx_indicator="#spinner",
            hx_trigger="load",
            cls=main_ctnr_cls,
        )

    def about_content():
        return fh.Main(
            fh.Div(
                fh.Div(
                    fh.P(
                        "I'm ",
                        fh.B(fh.U("Andrew Hinh")),
                        ", a 3rd year CSEN student at SCU focusing on ML/DL. In my free time, I enjoy cooking, gaming, and rock climbing.",
                    ),
                    fh.Img(
                        src="/assets/andrew.jpeg",
                        alt="Andrew's Profile Picture",
                        hx_indicator="#spinner",
                        hx_trigger="load",
                        cls="max-h-60 max-w-60 object-contain",
                    ),
                    cls="justify-between " + page_ctnt_cls,
                ),
                fh.Div(
                    fh.P(
                        "Hi, my name is ",
                        fh.B(fh.U("Pranav Chainani")),
                        " and I am a third-year Electrical and Computer Engineering major at Santa Clara University. My interests include circuit design, and artificial intelligence in embedded systems. I have experience as a Product Manager as I am going to embark on my third internship at Microsoft as a Product Manager Intern. My hobbies include hiking, playing basketball, and watching crime thrillers.",
                    ),
                    fh.Img(
                        src="/assets/pranav.jpeg",
                        alt="Pranav's Profile Picture",
                        hx_indicator="#spinner",
                        hx_trigger="revealed",
                        cls="max-h-60 max-w-60 object-contain",
                    ),
                    cls="justify-between " + page_ctnt_cls,
                ),
                fh.Div(
                    fh.P(
                        "Hi! My name is ",
                        fh.B(fh.U("Gigi")),
                        " and I am a Junior Electrical and Computer Engineering Major. I like to experiment with robotics and computer science, especially using Python and C. On campus, I am involved in the Society of Women Engineers (SWE), and in my free time, I like to travel, read, and spend time with friends.",
                    ),
                    fh.Img(
                        src="/assets/gigi.jpeg",
                        alt="Gigi's Profile Picture",
                        hx_indicator="#spinner",
                        hx_trigger="revealed",
                        cls="max-h-60 max-w-60 object-contain",
                    ),
                    cls="justify-between " + page_ctnt_cls,
                ),
                fh.Div(
                    fh.P(
                        "Hello there! My name is ",
                        fh.B(fh.U("Anastasiia Statcenko")),
                        " and I am a junior studying Computer Science and Engineering at Santa Clara University. I enjoy working on projects that combine my passion for programming and hardware, such as building an Autonomous Whack-A-Mole Robot or SQL-like Parser Client in C++. On campus, I am involved in Acapella and Choir. Outside of academics, I love reading philosophy and writing music.",
                    ),
                    fh.Img(
                        src="/assets/stasiia.jpeg",
                        alt="Stasiia's Profile Picture",
                        hx_indicator="#spinner",
                        hx_trigger="revealed",
                        cls="max-h-60 max-w-60 object-contain",
                    ),
                    cls="justify-between " + page_ctnt_cls,
                ),
                cls="md:w-2/3 flex flex-col md:grid md:grid-cols-2 gap-10",
            ),
            cls=main_ctnr_cls,
        )

    def partner_content():
        return fh.Main(
            fh.Div(
                fh.P(
                    "The ",
                    fh.A(
                        "Maternal Health Foundation",
                        href="https://maternalhealthfoundation.org",
                        cls=link_cls,
                    ),
                    """ (MHF) is a foundation working to decrease the rate of childbirth injuries suffered by women in sub-Saharan Africa. They work directly with these women through local healthcare clinics which they provide funding, allowing for both a higher quality of care and numerous classes educating women on pre and postnatal care. This holistic approach allows for both in-the-moment mitigation of injuries as well as long-term benefits by teaching preventative measures and educating the community as a whole on childbirth injuries. Educational outreach such as this is also key to the reintegration of women with previous childbirth injuries, as without proper care and information these women would continue to suffer. MHF also works with other local organizations such as the """,
                    fh.A("Terrewode Women's Hospital", href="https://terrewode.org/", cls=link_cls),
                    " in Uganda and ",
                    fh.A("Fistula e.V", href="https://www.fistula.de/", cls=link_cls),
                    " which both share similar goals of improving maternal health in sub-Saharan Africa. ",
                ),
                fh.Iframe(
                    src="https://www.youtube.com/embed/FpMZB5JoQJc", title="Fistula: An MHF Film", cls="w-full h-96"
                ),
                cls="md:w-2/3 justify-start " + page_ctnt_cls,
            ),
            hx_indicator="#spinner",
            hx_trigger="load",
            cls=main_ctnr_cls,
        )

    def blog_content():
        return fh.Main(
            fh.Div(
                fh.P("Weekly Reports", cls="text-4xl text-center"),
                cls="md:w-2/3 justify-center " + page_ctnt_cls,
            ),
            fh.Div(
                fh.P(
                    fh.B(fh.U("3/4/25")),
                ),
                fh.Ul(
                    fh.Li("Updated progress for draft of final report."),
                    fh.Li("Completed model fine-tune and API + website."),
                    fh.Li("Updated our Gantt chart."),
                ),
                fh.P(fh.B(fh.U("Andrew:"))),
                fh.Ul(
                    fh.Li("Completed model fine-tune and API + website."),
                    fh.Li("Emailed partner about model training progress."),
                    fh.Li("Updated the eFolio's blog page with new information."),
                ),
                fh.Iframe(
                    src="https://docs.google.com/document/d/1JlFB8ReklXnuTDAgMZ1R-huJg36f4kV9Y9CpOZrKLmI/edit?usp=sharing?embedded=true",
                    title="Week 8 Draft Report",
                    cls="w-full h-svh",
                    hx_indicator="#spinner",
                    hx_trigger="revealed",
                ),
                cls="md:w-2/3 " + page_ctnt_cls,
            ),
            fh.Div(
                fh.P(
                    fh.B(fh.U("2/25/25")),
                ),
                fh.Ul(
                    fh.Li("Reflected on our team's progress and our project's impact."),
                    fh.Li("Completed initial model fine-tune and draft API + website."),
                    fh.Li("Updated our Gantt chart."),
                ),
                fh.P(fh.B(fh.U("Andrew:"))),
                fh.Ul(
                    fh.Li("Completed initial model fine-tune and ran evaluation."),
                    fh.Li("Emailed partner about updated evaluation metrics."),
                    fh.Li("Updated the eFolio's blog page with new information."),
                ),
                fh.Iframe(
                    src="https://docs.google.com/document/d/1x5yxfhsUCS8gRAXRlKIHsDldSjluekfPUSum8A4VoRA/edit?usp=sharing?embedded=true",
                    title="Week 7 Reflection",
                    cls="w-full h-svh",
                    hx_indicator="#spinner",
                    hx_trigger="revealed",
                ),
                cls="md:w-2/3 " + page_ctnt_cls,
            ),
            fh.Div(
                fh.P(
                    fh.B(fh.U("2/18/25")),
                ),
                fh.Ul(
                    fh.Li("Emailed our community partner about the metric we've chosen to use for evaluation."),
                    fh.Li("Completed eFolio peer reviews."),
                    fh.Li("Updated our Gantt chart."),
                    fh.Li("Completed EDA and baseline evaluation."),
                    fh.Li("Presented on our project status to the class and our community partner."),
                ),
                fh.P(fh.B(fh.U("Andrew:"))),
                fh.Ul(
                    fh.Li(
                        "Completed EDA and baseline evaluation of model.",
                    ),
                    fh.Li(
                        "Emailed the metric we decided to use for evaluating the model to our community partner.",
                    ),
                    fh.Li(
                        "Updated the dataset, EDA, and model evaluation slides for the project status update presentation.",
                    ),
                    fh.Li("Updated the eFolio's blog page with new information."),
                ),
                fh.Iframe(
                    src="https://docs.google.com/presentation/d/1_ob0-vyQvwqZDx8aDCFRiMYe7fL2NOY54j6C7P7f68k/edit?usp=sharing?embedded=true",
                    title="Week 6 Status Update Presentation",
                    cls="w-full h-svh",
                    hx_indicator="#spinner",
                    hx_trigger="revealed",
                ),
                fh.Iframe(
                    src="https://docs.google.com/document/d/1a7lgvn6qnTkRB2bDayvsGMw8nEvdTFKilLsLrnjH5q4/edit?usp=sharing?embedded=true",
                    title="Week 6 Metrics",
                    cls="w-full h-svh",
                    hx_indicator="#spinner",
                    hx_trigger="revealed",
                ),
                cls="md:w-2/3 " + page_ctnt_cls,
            ),
            fh.Div(
                fh.P(
                    fh.B(fh.U("2/11/25")),
                ),
                fh.P(fh.B(fh.U("Andrew:"))),
                fh.Ul(
                    fh.Li(
                        "Started work on implementation of accepted solution.",
                    ),
                    fh.Li("Wrote the roadmap for the project report introduction."),
                    fh.Li("Updated the eFolio's blog page with new information."),
                ),
                fh.Ul(
                    fh.Li("Met with our community partner to discuss ranking of proposed solutions we will use."),
                    fh.Ul(
                        fh.Li(
                            "We settled on fine-tuning Qwen2.5-VL on the point-prediction task using our proposed dataset.",
                            cls="list-disc list-inside",
                        ),
                        fh.Li(
                            "For the implementation, he'd like us to focus on finding good metrics for evaluation, minimizing latency and memory usage, and comparing the performance of different model sizes.",
                            cls="list-disc list-inside",
                        ),
                        cls="flex flex-col gap-1 p-2",
                    ),
                    fh.Li("Scheduled a meeting with our community partner to check in on our implementation progress."),
                    fh.Li("Updated our Gantt chart."),
                    fh.Li("Wrote the introduction for our project report."),
                ),
                fh.Iframe(
                    src="https://docs.google.com/document/d/1099_lKw-ioY0NKNFFzv7Kf-yvIcjKzkDrbEGmVqU6fA/edit?usp=sharing?embedded=true",
                    title="Week 5 Project Report Introduction",
                    cls="w-full h-svh",
                    hx_indicator="#spinner",
                    hx_trigger="revealed",
                ),
                cls="md:w-2/3 " + page_ctnt_cls,
            ),
            fh.Div(
                fh.P(
                    fh.B(fh.U("2/4/25")),
                ),
                fh.P(fh.B(fh.U("Andrew:"))),
                fh.Ul(
                    fh.Li(
                        "Researched majority of solutions to propose to our community partner.",
                    ),
                    fh.Li("Revised team contract."),
                    fh.Li("Revised and added thoughts to team reflection."),
                    fh.Li("Updated the eFolio's blog page with new information."),
                ),
                fh.Ul(
                    fh.Li(
                        "Met with our community partner to discuss ranking of proposed datasets we will use. Below is the summary:",
                        fh.Ul(
                            fh.Li(
                                "Mahni agreed with our ranking, and proposed his own dataset which we initially rejected due to the lack of segmentation labels. However, he now says these labels are not necessarily required.",
                                cls="list-disc list-inside",
                            ),
                            cls="flex flex-col gap-1 p-2",
                        ),
                    ),
                    fh.Li(
                        "Scheduled a meeting with our community partner to discuss proposed solutions for the project."
                    ),
                    fh.Li("Researched solutions to propose to our community partner."),
                    fh.Li("Updated our Gantt chart."),
                    fh.Li("Reflected on our team's progress and our project's impact."),
                ),
                fh.Iframe(
                    src="https://docs.google.com/document/d/1QKPghn7ofOXiDgwf9LgjZudIWcZalDaYbgZFZymEgaU/edit?usp=sharing?embedded=true",
                    title="Week 4 Solution Proposal",
                    cls="w-full h-svh",
                    hx_indicator="#spinner",
                    hx_trigger="revealed",
                ),
                fh.Iframe(
                    src="https://docs.google.com/document/d/1mfdwgn7euTwjL1cV9o15PlTjvGGw1HAhCUs9rCUpKAk/edit?usp=sharing?embedded=true",
                    title="Week 4 Design Review",
                    cls="w-full h-svh",
                    hx_indicator="#spinner",
                    hx_trigger="revealed",
                ),
                cls="md:w-2/3 " + page_ctnt_cls,
            ),
            fh.Div(
                fh.P(
                    fh.B(fh.U("1/28/25")),
                ),
                fh.P(fh.B(fh.U("Andrew:"))),
                fh.Ul(
                    fh.Li(
                        "Researched datasets to propose to our community partner, including ",
                        fh.A("this dataset", href="https://www.nature.com/articles/s41597-024-03774-3", cls=link_cls),
                        " which we will proceed with for the project.",
                    ),
                    fh.Li("Updated the eFolio's blog page with new information."),
                ),
                fh.Ul(
                    fh.Li(
                        "Came up with the following problem statement:",
                        fh.Ul(
                            fh.Li(
                                "MHF’s Chief AI Officer needs a potential automated solution to suggest labels for ultrasound images because of the time and monetary cost of manual labor.",
                                cls="list-disc list-inside",
                            ),
                            cls="flex flex-col gap-1 p-2",
                        ),
                    ),
                    fh.Li(
                        "Scheduled a meeting with our community partner to discuss proposed datasets we will use. Below is the summary:",
                    ),
                    fh.Li("Researched datasets to propose to our community partner."),
                    fh.Li("Revised our Gantt chart to include more details."),
                    fh.Li("Created a team contract."),
                    fh.Li(
                        "Met with our community partner to discuss proposed datasets we will use. Below is the summary:",
                        fh.Ul(
                            fh.Li(
                                "Before team meeting sunday, look over your and others' datasets and rank which ones you think we should use. We’ll discuss it sunday and move forward with the top dataset to create a proposal for him for our meeting next week.",
                                cls="list-disc list-inside",
                            ),
                            cls="flex flex-col gap-1 p-2",
                        ),
                    ),
                    fh.Li(
                        "Scheduled another meeting with our community partner to discuss ranking of proposed datasets."
                    ),
                ),
                fh.Iframe(
                    src="https://docs.google.com/document/d/1wMQcTuM_cb2Ur1VsG8rVsLqLigFYQLwoaBg-8dgU9Nk/edit?usp=drive_link?embedded=true",
                    title="Week 3 Dataset Proposal",
                    cls="w-full h-svh",
                    hx_indicator="#spinner",
                    hx_trigger="revealed",
                ),
                fh.Iframe(
                    src="https://docs.google.com/spreadsheets/d/1xF2eMSg26GFkbdGwVVUvcIv7fqNWWWDsGyeHeZoppdU/edit?usp=drive_link?embedded=true",
                    title="Week 3 Gantt Chart",
                    cls="w-full h-svh",
                    hx_indicator="#spinner",
                    hx_trigger="revealed",
                ),
                fh.Iframe(
                    src="https://docs.google.com/document/d/1KObr86ITkrr6Qc9P0LxuaFamLGa7eYNdOq9UDD2aIAI/edit?usp=drive_link?embedded=true",
                    title="Week 3 Team Contract",
                    cls="w-full h-svh",
                    hx_indicator="#spinner",
                    hx_trigger="revealed",
                ),
                cls="md:w-2/3 " + page_ctnt_cls,
            ),
            fh.Div(
                fh.P(
                    fh.B(fh.U("1/21/25")),
                ),
                fh.P(fh.B(fh.U("Andrew:"))),
                fh.Ul(
                    fh.Li("Researched a few datasets before the meeting with our community partner."),
                    fh.Li(
                        "Updated the eFolio to add the partner page, and updated the About us and project pages with new information."
                    ),
                    fh.Li("Created a new GH repo for all of our work we will share with our community partner."),
                    fh.Li("Gave initial draft for distributing phases amongst team members."),
                ),
                fh.Ul(
                    fh.Li(
                        "Scheduled a meeting with our community partner, and drafted questions and curated datasets in preparation."
                    ),
                    fh.Li("Met with our community partner and collected extensive notes."),
                    fh.Li("Estimated our project timeline by creating a Gantt chart."),
                    fh.Li("Created a new GH repo for all of our work we will share with our community partner."),
                    fh.Li(
                        "Scheduled another meeting with our community partner to discuss the project timeline and next steps."
                    ),
                ),
                fh.Iframe(
                    src="https://docs.google.com/document/d/1UrzQ3rnxGRUNtGPX4nH8FHaKZ-VpXASbr3uJJ8OQVZw/edit?usp=drive_link?embedded=true",
                    title="Week 2 Team Activities and Documentation",
                    cls="w-full h-svh",
                    hx_indicator="#spinner",
                    hx_trigger="revealed",
                ),
                cls="md:w-2/3 " + page_ctnt_cls,
            ),
            fh.Div(
                fh.P(
                    fh.B(fh.U("1/14/25")),
                ),
                fh.P(
                    "This is my first choice partner because I really enjoy working on AI, especially when applied to healthcare.",
                ),
                fh.Iframe(
                    src="https://docs.google.com/document/d/14YZgGb4Hw2yzWcnKXt-fEAJYrAUGvkSgd10AhLYwkW4/edit?usp=drive_link?embedded=true",
                    title="Andrew's CP Research",
                    cls="max-w-60 max-h-60 object-contain",
                    hx_indicator="#spinner",
                    hx_trigger="revealed",
                ),
                cls="md:w-2/3 " + page_ctnt_cls,
            ),
            cls=main_ctnr_cls,
        )

    def toast_container():
        return fh.Div(id="toast-container", cls="hidden")

    def footer():
        return fh.Footer(
            fh.A(
                fh.Svg(
                    fh.NotStr(
                        si_github.svg,
                    ),
                    cls="w-8 h-8 text-blue-300 hover:text-blue-100 cursor-pointer",
                ),
                href="https://github.com/andrewhinh/mhf",
                target="_blank",
            ),
            fh.Div(
                fh.P("Made by"),
                fh.A(
                    "Andrew Hinh",
                    href="https://ajhinh.com/",
                    cls="font-bold " + link_cls,
                ),
                cls="flex flex-col text-right gap-0.5",
            ),
            cls="flex justify-between items-center p-4 text-lg",
        )

    # routes
    ## for images, CSS, etc.
    @f_app.get("/{fname:path}.{ext:static}")
    def static_files(fname: str, ext: str):
        static_file_path = PARENT_PATH / "assets" / f"{fname}.{ext}"
        print(static_file_path, static_file_path.exists())
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
                home_content(),
                toast_container(),
                footer(),
                cls=page_cls,
            ),
        )

    @f_app.get("/about-us")
    def about_us(
        session,
    ):
        return (
            fh.Title(NAME + " | " + "about us"),
            fh.Div(
                nav(),
                about_content(),
                toast_container(),
                footer(),
                cls=page_cls,
            ),
        )

    @f_app.get("/partner")
    def partner(
        session,
    ):
        return (
            fh.Title(NAME + " | " + "partner"),
            fh.Div(
                nav(),
                partner_content(),
                toast_container(),
                footer(),
                cls=page_cls,
            ),
        )

    @f_app.get("/blog")
    def blog(
        session,
    ):
        return (
            fh.Title(NAME + " | " + "blog"),
            fh.Div(
                nav(),
                blog_content(),
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
        "python-fasthtml>=0.12.0",
        "simpleicons>=7.21.0",
        "sqlite-minutils>=4.0.3",
    )
    .add_local_dir(PARENT_PATH / "assets", "/root/assets", copy=True)
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

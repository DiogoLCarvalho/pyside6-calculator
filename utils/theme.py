# qdarktheme available below python 11 version
import qdarktheme

# colors of buttons
qss_light = """ 
    QPushButton[cssClass="resultButton"] {
        color: #fff;
        background: "#373F42";
    }
    QPushButton[cssClass="resultButton"]:hover {
        color: #fff;
        background: "#4A5154";
    }
    QPushButton[cssClass="resultButton"]:pressed {
        color: #fff;
        background: "#5D6365";
    }
    QPushButton[cssClass="borderButton"] {
        color: #5D5D5D;
        background: "#F9F9F9";
    }
    QPushButton[cssClass="borderButton"]:hover {
        color: #5D5D5D;
        background: "#F6F6F6";
    }
    QPushButton[cssClass="borderButton"]:pressed {
        color: #5D5D5D;
        background: "#F4F4F4";
    }
    QPushButton{
        color: #1B1B1B;
        background: "#FFFFFF";
    }
    QLineEdit{
        border-width: 0px;
        color: #000000;
    }
"""

qss_dark = """ 
    QPushButton[cssClass="resultButton"] {
        color: #E2E2E2;
        background: "#343334";
    }
    QPushButton[cssClass="resultButton"]:hover {    
        color: #E2E2E2;
        background: "#484644";
    }
    QPushButton[cssClass="resultButton"]:pressed {
        color: #E2E2E2;
        background: "#4C4A48";
    }
    QPushButton[cssClass="borderButton"] {
        color: #FFFFFF;
        background: "#161618";
    }
    QPushButton[cssClass="borderButton"]:hover {
        color: #FFFFFF;
        background: "#4D4E51";
    }
    QPushButton[cssClass="borderButton"]:pressed {
        color: #FFFFFF;
        background: "#606164";
    }
    QPushButton{
        color: #FFFFFF;
        background: "#070708";
    }
    QLineEdit{
        border-width: 0px;
        color: #FFFFFF;
    }
"""

def setupTheme(themeChoise : str = "light"):
    qss = qss_light if themeChoise == "light" else qss_dark

    qdarktheme.setup_theme(
        theme=themeChoise,
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": "#4E4F51",
            },
            "[light]": {
                "primary": "#5D5D5D",
            },
        },
        additional_qss=qss
)
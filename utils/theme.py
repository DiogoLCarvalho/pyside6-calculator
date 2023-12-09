# qdarktheme available below python 11 version
import qdarktheme

# colors of buttons
qss = """ 
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
    }
"""

def setupTheme():
    qdarktheme.setup_theme(
        theme="light",
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": "#1e81b0",
            },
            "[light]": {
                "primary": "#5D5D5D",
            },
        },
        additional_qss=qss
)
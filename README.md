# Graph Maker

![License](https://img.shields.io/badge/license-MIT-green)
![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)

## Description
Graph Maker is a Python application that communicates with Arduino via serial port to visualize real-time data in graph form. It features a graphical user interface built with PyQt, which allows users to interactively visualize data streamed from Arduino sensors.

## Installation
### Prerequisites
- Python 3.8 or newer
- PyQt5
- An Arduino board
- Arduino IDE (to upload sketches to the Arduino)

### Setup
1. **Arduino Setup**:
   - Connect your Arduino to your computer.
   - Open Arduino IDE, upload the provided sketch to read from the desired sensors.
   - Ensure the serial communication is set correctly (baud rate, etc.).

2. **Software Setup**:
   - Clone this repository:
     ```sh
     git clone https://github.com/yourusername/graph_maker.git
     ```
   - Install the required Python dependencies:
     ```sh
     pip install pyqt5 serial
     ```
   - Navigate to the project directory and run the main script:
     ```sh
     python main_ui.py
     ```

## Usage
Launch the Graph Maker by executing `main_ui.py`. Make sure the Arduino is connected and transmitting data. Use the GUI to start receiving and plotting data from Arduino. Adjust settings as necessary for different sensors or data rates.

## Contributing
This project is no longer actively maintained. For major issues or enhancements, please consider forking the repository to make improvements.

## Contact
For support or specific inquiries related to this project, please contact via email: [yumsan1305@gmail.com].

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

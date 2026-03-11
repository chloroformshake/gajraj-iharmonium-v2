# i-harmonium

A web-based harmonium that uses your laptop's lid angle to control the bellows (air pressure). Press keys and push your laptop lid down to play!

## How It Works

- **Keys**: Press keyboard keys (A, W, S, E, D, F, T, G, Y, H, U, J, K) to play notes
- **Bellows**: Close your laptop lid (push down) to pump air and produce sound
- **Lid Angle Sensor**: Python backend reads your laptop's lid angle in real-time
- **WebSocket Connection**: Sends lid angle data to the HTML interface
- **Sound Generation**: Web Audio API creates harmonium-like tones

## Requirements

- Python 3.7+
- `websockets` library
- `pybooklid` library (for MacBook lid sensor)
- A web browser (Chrome, Firefox, Safari, etc.)
- A MacBook with a working lid angle sensor

## Installation

1. **Set up a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install required Python packages**:
   ```bash
   pip install websockets pybooklid
   ```

## Running the Harmonium

### Step 1: Start the Backend

First, run the Python WebSocket server that reads your laptop's lid angle:

```bash
python harmonium.py
```

You should see:
```
Bridge active! Waiting for your web app on port 8765...
```

### Step 2: Open the HTML File

Open `harmonium.html` in your web browser:

```bash
open harmonium.html
```

Or simply double-click the `harmonium.html` file.

### Step 3: Activate Audio

- Click anywhere on the page once to activate audio (browser security requirement)
- You should see "Audio Active - Ready to play"

### Step 4: Play!

1. **Press and hold** any of these keys: A, W, S, E, D, F, T, G, Y, H, U, J, K
2. **Push your laptop lid down** (close it partially) to pump air
3. The bellows meter will fill up as you close the lid
4. Sound will play based on how much air is in the bellows!

## Key Mapping

```
White Keys (Natural Notes):
A = C
S = D
D = E
F = F
G = G
H = A
J = B
K = C (octave)

Black Keys (Sharps):
W = C#
E = D#
T = F#
Y = G#
U = A#
```

## Tips

- The harder/faster you close the lid, the more air you pump
- Air slowly leaks out, just like a real harmonium
- Hold multiple keys simultaneously for chords
- The lid angle is displayed at the top of the interface

## Troubleshooting

**No sound?**
- Make sure you clicked on the page to activate audio
- Check that your system volume is up
- Verify the Python backend is running

**WebSocket connection failed?**
- Ensure `harmonium.py` is running first
- Check that port 8765 is not in use by another application
- Look for "Web App connected!" message in the Python terminal

**Lid angle not changing?**
- Verify `pybooklid` is properly installed
- Check that your MacBook's lid sensor is working
- Try closing and opening the lid to see if values change

## Stopping

- **Backend**: Press `Ctrl+C` in the terminal running `harmonium.py`
- **Frontend**: Simply close the browser tab

## License

Feel free to use and modify this project as you wish!

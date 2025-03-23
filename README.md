# Hikvision_Poc_shodan

This project is a Python tool designed to check the security of IP cameras detected on the network using the Shodan API. Users can perform a search for "ip camera" on Shodan and check if each camera has a security vulnerability by accessing a specific URL.

## Requirements

- Python 3.x
- Shodan API key
- `requests` and `shodan` Python libraries
  - To install these libraries, you can use the following commands in your terminal:
    ```
    pip install requests
    pip install shodan
    ```

## Usage

1. **Obtain your Shodan API Key**:
   - To get your Shodan API key, sign up at [Shodan](https://www.shodan.io/) and obtain your key.

2. **Run the Python Script**:
   - After you have the script and your API key ready, run the Python script:
     ```bash
     python shodan_ip_camera_security_check.py
     ```

3. **Select Your Search Option**:
   - When prompted, choose whether to search using Shodan (`s`) or provide a manual IP (`m`).

4. **View the Results**:
   - The script will show you if each camera found via Shodan is vulnerable based on the response from the provided URL.

## How It Works

- The script connects to Shodan's search API and looks for devices matching the "ip camera" query.
- It then attempts to access a predefined snapshot URL for each camera to check if it is vulnerable by sending HTTP requests with authentication.
- The script also allows checking a manually provided IP address.

## Example


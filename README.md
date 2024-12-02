# Market router: Market Neutral Provider
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Website](https://img.shields.io/badge/Visit-marketrouter.ai-blue)](https://marketrouter.ai)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/GroupLang.svg?style=social&label=Follow%20%40GroupLang)](https://twitter.com/GroupLang)

## Overview

This system acts as a counterpart to the [Market Neutral Requester](https://github.com/GroupLang/neutral-portfolio-requester), focusing on analyzing sector-specific news to generate actionable insights for stock decisions. It utilizes the [Market router API](https://marketrouter.ai/) for all interactions and integrates with an OpenAI completions endpoint to process news inputs supplied by the requester, subsequently generating investment recommendations.

<p align="center">
  <img src="https://github.com/user-attachments/assets/9b29a7bc-5b89-4c67-9336-2249f0569d00" alt="MarketNeutral (10)" width="500">
</p>

## Installing pip

Before you can install the required libraries for this project, you need to have pip installed. Pip is the package installer for Python and is used to install and manage software packages.

### Windows

1. Download the get-pip.py file from https://bootstrap.pypa.io/get-pip.py.
2. Open a command prompt and navigate to the directory where you downloaded get-pip.py.
3. Run the following command:
   ```shell
   python get-pip.py
   ```

### macOS and Linux

Pip is usually installed by default with Python. You can check if pip is installed by running:
```shell
pip --version
```

If pip is not installed, you can install it using the following command:
```shell
python3 -m ensurepip --upgrade
```

## Why Use Docker in Software Engineering Projects

Docker is a powerful tool in software engineering that provides several benefits:

1. **Consistency Across Environments**: Docker ensures that the software runs the same way regardless of where it is deployed. This eliminates the "it works on my machine" problem by using containerization to encapsulate the application and its dependencies.

2. **Simplified Deployment**: Docker containers can be easily deployed to any environment that supports Docker, making it straightforward to move applications from development to production.

3. **Scalability**: Docker makes it easy to scale applications horizontally by running multiple instances of a containerized application across a cluster of machines.

4. **Isolation**: Each Docker container runs in its own isolated environment, which helps in managing dependencies and avoiding conflicts between different applications running on the same host.

5. **Resource Efficiency**: Docker containers are lightweight and share the host system's kernel, which makes them more resource-efficient compared to traditional virtual machines.

By using Docker, this project ensures that all contributors and users can work in a consistent environment, reducing the chances of encountering environment-specific issues.

1. **Clone the repository**

   ```shell
   git clone https://github.com/GroupLang/market-neutral-provider.git
   cd market-neutral-provider
   ```
2. **Install required libraries**
   ```shell
   python3.11 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Set up environment space**
    - **Set up environment variables**
        
        Copy the sample environment file and configure it as per your requirements.

        ```shell
        [ ! -f .env ] && cp .env.template .env
        ```


## Configuration

- **Market router**:
  - **Username, Fullname, Email, Password**: These credentials are used for authentication and identification in the market router. If the user is already registered, these parameters are not necessary; instead, add the Market router API key to the `.env` file as `MARKET_ROUTER_API_KEY`
  - **Deposit Amount**: Specify the initial deposit amount for transactions in the market router if needed.
  
- **Proposal**:
  - **Endpoint**: Define the API endpoint for proposal submissions. Used by market router when requester calls `completions` endpoint in order to obtain OpenAI wrapper response.
  - **Max Bid**: Determines the maximum bid amount for proposals. If set to None, a gpt-4o-mini model will decide the appropriate bid based on the instance's background. This part of the configuration directly impacts the economic considerations of the proposals.

These configuration variables are stored in the config file, ensuring the Market Neutral Provider can effectively interact with the Market router by managing its proposals and financial transactions.

## Key Components and Processes

**Market router Scripts:**
1. **Register User Script**
   ```shell
   python -m market_router.scripts.register
   ```
   This command registers a new user with the Market router API. If `MARKET_ROUTER_API_KEY` exists (indicating prior registration), this script is unnecessary.

2. **Create API Key Script**
   ```shell
   python -m market_router.scripts.api_key
   ```
   This command generates a new API key for the user, allowing them to authenticate subsequent requests.

3. **Deposit Script**
   ```shell
   python -m market_router.scripts.deposit
   ```
   This command facilitates depositing funds into an Market router account, as specified in the `deposit_amount` configuration.

4. **Create Proposal Script**
   ```shell
   python -m market_router.scripts.proposal
   ```
   This script submits proposals to the Market router using configured `endpoint` and `max_bid` settings, detailing the financial and operational parameters for engagements.

**API Services Scripts:**
1. **Model Response Script**
   ```shell
   python -m api.services.model_response --model_args='{"messages": [{"role": "user", "content": "Test OpenAI Wrapper"}], "model": "gpt-3.5-turbo", "temperature": 0.5}'
   ```
   This command generates simulated responses from the model, designed to test the API's capability to process and respond to input accurately under controlled settings.

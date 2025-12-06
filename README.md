# Physical AI & Humanoid Robotics

This repository contains the Docusaurus project for the "Physical AI & Humanoid Robotics" book.

## Project Structure

- `website/`: Contains the Docusaurus documentation site.
- `specs/`: Contains the specification documents for each module/feature.
- `history/`: Stores prompt history records and architectural decision records.

## Local Development

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/my-org/my-book.git
    cd my-book
    ```
2.  **Install Docusaurus dependencies**:
    ```bash
    cd website
    npm install
    ```
3.  **Start the development server**:
    ```bash
    npm run start
    ```
    This command starts a local development server and opens a browser window. Most changes are reflected live without restarting the server.

## Build

```bash
npm run build
```
This command generates static content into the `build` directory and can be served using any static content hosting service.

## Deployment

The `website` folder can be deployed to GitHub Pages by following the Docusaurus deployment guide.

mkdir -p .devcontainer
cat <<EOL > .devcontainer/devcontainer.json
{
"name": "My Workflow",
"image": "mcr.microsoft.com/workflow/devcontainers/python:3.8",
"features": {
"ghcr.io/devcontainers/features/sshd:1": {
"version": "latest"
}
},
"postStartCommand": "python3 /workspaces/Gumnaam/GumnaamGhs.py",
"customizations": {
"workflow": {
"settings": {
"python.pythonPath": "/usr/local/bin/python"
},
"extensions": [
"ms-python.python"
]
}
}
}
EOL
git add .devcontainer/devcontainer.json
git commit -m "Add postStartCommand to run Python script automatically"
git push origin main



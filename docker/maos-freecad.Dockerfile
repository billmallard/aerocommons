# maos-freecad.Dockerfile
# Docker image for MAOS parametric CAD environment
# Contains: FreeCAD (headless + GUI via Xvfb), Python scripting
# Build: docker build -f maos-freecad.Dockerfile -t maos-freecad:latest .

FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

# Install FreeCAD and dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common \
    && add-apt-repository -y ppa:freecad-maintainers/freecad-stable \
    && apt-get update \
    && apt-get install -y \
    freecad \
    freecad-python3 \
    xvfb \
    wget \
    curl \
    git \
    python3-pip \
    python3-numpy \
    python3-matplotlib \
    && rm -rf /var/lib/apt/lists/*

# Virtual framebuffer display for headless FreeCAD GUI operations
ENV DISPLAY=:99

# Create working directory for CAD files
WORKDIR /workspace
RUN chmod 777 /workspace

# Mount point for agent CAD files (bind-mounted at runtime)
RUN mkdir -p /workspace/cad

# Verify installation
RUN freecadcmd --version 2>&1 || echo "FreeCAD CMD not found"

# Start Xvfb, then drop to shell
CMD ["bash", "-c", "Xvfb :99 -screen 0 1024x768x24 &>/dev/null & sleep 1; echo 'MAOS FreeCAD Ready'; freecadcmd --version 2>&1; exec bash"]

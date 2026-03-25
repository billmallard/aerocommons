# maos-aero-tools.Dockerfile
# Docker image for MAOS aerodynamic analysis tools
# Contains: OpenVSP, AVL (MIT)
# Build: docker build -f maos-aero-tools.Dockerfile -t maos-aero-tools:latest .

FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

# Install base dependencies + Xvfb for headless display
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    wget \
    curl \
    ca-certificates \
    libx11-dev \
    libgl1-mesa-dev \
    libglu1-mesa-dev \
    libxrandr-dev \
    libxinerama-dev \
    libxcursor-dev \
    libxi-dev \
    libfreetype6-dev \
    libfontconfig1-dev \
    gfortran \
    unzip \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Virtual framebuffer display for headless OpenVSP
ENV DISPLAY=:99

# Install OpenVSP 3.48.2 from official .deb package
WORKDIR /opt
RUN wget -q "https://openvsp.org/download.php?file=zips/current/linux/OpenVSP-3.48.2-Ubuntu-24.04_amd64.deb" \
        -O OpenVSP-3.48.2.deb \
    && apt-get update \
    && apt-get install -y desktop-file-utils ./OpenVSP-3.48.2.deb \
    && rm OpenVSP-3.48.2.deb \
    && rm -rf /var/lib/apt/lists/*

# Install AVL (Athena Vortex Lattice) 3.40b
# Pre-built Linux 64-bit binary from MIT
WORKDIR /opt
RUN wget -q https://web.mit.edu/drela/Public/web/avl/avl3.40_execs/LINUX64/avl \
        -O /usr/local/bin/avl \
    && chmod +x /usr/local/bin/avl

# Create working directory for analysis
WORKDIR /workspace
RUN chmod 777 /workspace

# Mount point for AERO agent analysis files (bind-mounted at runtime)
RUN mkdir -p /workspace/analysis

# Verify installations
RUN which vspscript && echo "OpenVSP vspscript installed" || echo "OpenVSP install failed" \
    && which vspaero && echo "VSPAero installed" || echo "VSPAero install failed" \
    && which avl && echo "AVL installed" || echo "AVL install failed"

# Start Xvfb, then drop to shell
CMD ["bash", "-c", "Xvfb :99 -screen 0 1024x768x24 &>/dev/null & sleep 1; echo 'MAOS Aero Tools Ready'; echo 'OpenVSP:'; vspscript -help 2>&1 | head -5 || echo 'vspscript not found'; echo 'AVL:'; echo 'quit' | avl 2>&1 | head -10; exec bash"]

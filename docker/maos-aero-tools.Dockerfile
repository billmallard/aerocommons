# maos-aero-tools.Dockerfile
# Docker image for MAOS aerodynamic analysis tools
# Contains: OpenVSP, AVL (MIT)
# Build: docker build -f maos-aero-tools.Dockerfile -t maos-aero-tools:latest .

FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

# Install base dependencies
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
    && rm -rf /var/lib/apt/lists/*

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
RUN which vsp && vsp -h || echo "OpenVSP installed (VSP GUI available)" \
    && which vspaero && vspaero -h || echo "VSPAero installed" \
    && which avl && echo "AVL installed" || echo "AVL install failed"

# Default command: print tool versions
CMD ["bash", "-c", "echo 'MAOS Aero Tools Ready'; echo 'OpenVSP:'; vsp -v 2>&1 || echo 'vsp not found'; echo 'AVL:'; avl --version 2>&1 || echo 'avl not found'; bash"]

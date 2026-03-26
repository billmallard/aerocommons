# maos-calculix.Dockerfile
# Docker image for MAOS structural FEA environment
# Contains: CalculiX (ccx solver + cgx pre/post), Gmsh mesher
# Build: docker build -f maos-calculix.Dockerfile -t maos-calculix:latest .

FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

# Install CalculiX, Gmsh, and dependencies
RUN apt-get update && apt-get install -y \
    calculix-ccx \
    calculix-cgx \
    gmsh \
    python3 \
    python3-numpy \
    python3-matplotlib \
    xvfb \
    wget \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Virtual framebuffer display for headless cgx pre/post-processing
ENV DISPLAY=:99

# Create working directory for FEA files
WORKDIR /workspace
RUN chmod 777 /workspace

# Mount point for agent FEA files (bind-mounted at runtime)
RUN mkdir -p /workspace/fea

# Verify installations
RUN ccx -v 2>&1 | head -5 || echo "CalculiX ccx not found" \
    && which cgx && echo "CalculiX cgx installed" || echo "cgx not found" \
    && gmsh --version 2>&1 || echo "Gmsh not found"

# Start Xvfb, then drop to shell
CMD ["bash", "-c", "Xvfb :99 -screen 0 1024x768x24 &>/dev/null & sleep 1; echo 'MAOS CalculiX Ready'; ccx -v 2>&1 | head -3; echo 'Gmsh:'; gmsh --version 2>&1; exec bash"]

FROM minizinc/minizinc

COPY ./ /SPL-Solver
WORKDIR /SPL-Solver

RUN apt-get update && apt-get install -y \
    python3 \
    python3-distutils \
    python3-dev \
    curl \
    gcc \
    g++ \
    unzip

RUN ./pants package src/python/variamos/apps/solvers

ENTRYPOINT ["./dist/src.python.variamos.apps.solvers/solvers.pex"]

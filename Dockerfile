FROM julia:1.8.2-bullseye
RUN useradd -mG sudo julio
USER julio
WORKDIR /home/julio
COPY . .
RUN julia --project=. -e "using Pkg; Pkg.instantiate(); Pkg.precompile()"&&\
    mkdir output
CMD [ "julia", "--project=.","analisis_script.jl" ]
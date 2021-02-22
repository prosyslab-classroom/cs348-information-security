FROM ubuntu:18.04

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:avsm/ppa && \
    apt-get install -y make git gcc ocaml opam pkg-config m4 cmake sudo python2.7

ENV OCAML_VERSION=4.11.0
ENV CS448_OPAM_SWITCH=cs448-$OCAML_VERSION
ENV OPAMYES=1
ENV HOME=/home/student

RUN useradd -ms /bin/bash student

ENV SCRIPT=$HOME/script
RUN mkdir -p $SCRIPT
COPY install-llvm-toolchain.sh $SCRIPT
RUN $SCRIPT/install-llvm-toolchain.sh

RUN opam init --compiler=$OCAML_VERSION --disable-sandboxing && \
    opam switch create $CS448_OPAM_SWITCH $OCAML_VERSION && \
    eval $(opam env) && \
    opam install dune llvm.10.0.0 ounit

RUN echo "$(opam env)" >> ~/.bashrc
RUN sudo adduser student sudo
RUN echo "root:1234" | chpasswd
RUN echo "student:1234" | chpasswd
USER student
WORKDIR $HOME

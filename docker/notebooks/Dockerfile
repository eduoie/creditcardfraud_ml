FROM continuumio/miniconda3:4.10.3p0

RUN conda create -n notebooks python=3.6
RUN echo "source activate notebooks" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH

ADD dependencies dependencies

RUN conda env update -f /dependencies/notebooks.yml

EXPOSE 8888

SHELL ["/bin/bash", "-c"]
ENTRYPOINT source activate notebooks && \
           jupyter notebook --no-browser --allow-root --ip="0.0.0.0"

#ENTRYPOINT ["jupyter", "notebook", "--no-browser", "--allow-root", "--ip=0.0.0.0"]
 # "--NotebookApp.token=''", "--NotebookApp.password=''"]
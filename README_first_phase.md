## How to run

You can build the notebooks Docker image using `build_notebook_image.sh`, and then run it with `run_notebooks_image`

Open a terminal and execute: `jupyter  notebook --no-browser --allow-root --ip="0.0.0.0"`. Open Jupyter from the log link and tinker with it.

###Some useful references

https://towardsdatascience.com/making-docker-and-conda-play-well-together-eda0ff995e3c

https://github.com/borundev/jupyter_ml_docker/blob/deedede66b39e5c5f98f0fc51707a021611f4661/Dockerfile

https://uwekorn.com/2021/03/01/deploying-conda-environments-in-docker-how-to-do-it-right.html

https://stackoverflow.com/questions/28320134/how-can-i-list-all-tags-for-a-docker-image-on-a-remote-registry

[Matthijs Brouns - 10x smaller docker containers for Data Science | PyData Eindhoven 2020](https://www.youtube.com/watch?v=Z1Al4I4Os_A): around 5x in practical terms


docker run \
-p8888:8888 \
-d \
--name notebooks_container \
-ti --rm \
-v "$(pwd)"/notebooks:/notebooks \
-v "$(pwd)"/data:/data \
notebooks_image

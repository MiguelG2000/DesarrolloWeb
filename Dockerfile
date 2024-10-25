FROM ubuntu:latest
LABEL authors="mikegonzalez"

ENTRYPOINT ["top", "-b"]
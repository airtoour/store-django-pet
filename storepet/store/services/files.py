import uuid


def handle_upload_file(f):
    with open(f"uploads/{f.name}__{uuid.uuid4()}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

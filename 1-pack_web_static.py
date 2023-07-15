from fabric.api import local
from datetime import datetime
import os


def do_pack():
    # Get the cuurent date and time
    now = datetime.now().strftime("%Y%m%d%H%M%S")

    # Create the versions folder if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Set the name of the archive file
    archive_name = "web_static_" + now + ".tgz"

    # Create the archive by compressing the web_static folder
    result = local("tar -czvf versions/{} web_static".format(archive_name))

    # Check if the archive was created successfully
    if result.succeeded:
        return "version/" + archive_name
    else:
        return None

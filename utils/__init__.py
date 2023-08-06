import pathlib


def logo_directory_path(instance, filename):
    file_extensions = pathlib.Path(filename).suffix
    file_name = instance.slug
    path = "company/logo/images/"
    return "{0}/{1}.{2}".format(path, file_name, file_extensions)


def get_populate_from_name(instance):
    return '%s' % instance.name

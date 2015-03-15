db.define_table(
    'cms_clone',
    Field('url'),
    Field('html','text'),
    auth.signature)

db.define_table(
    'cms_folder',
    Field('name',requires=IS_NOT_EMPTY()),
    Field('parent_folder','reference cms_folder',readable=False,writable=False),
    auth.signature,
    format='%(name)s')

db.define_table(
    'cms_file',
    Field('folder','reference cms_folder',readable=False,writable=False),
    Field('name',requires=IS_NOT_EMPTY()),
    Field('file','upload'),
    auth.signature,
    format='%(name)s')


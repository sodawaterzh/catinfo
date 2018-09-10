from app import db,create_app
from app.models import catinfo
app = create_app()
#
# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'catinfo': catinfo}

if __name__ == '__main__':
	app.jinja_env.auto_reload = True
	# app.run(host='0.0.0.0',port=5001,)
	app.run(port=50001)

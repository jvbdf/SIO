import os
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from app.config import Config
from app.utils import get_user_by_id, login_required
from app.extensions import db
from app.utils import get_user_by_id

profile = Blueprint('profile',__name__)

@profile.route('/profile', methods = ['GET','POST'])
@login_required
def profile_page():
    
    user = get_user_by_id(session['user_id'])
    if request.method == 'POST':
        user.address = request.form['address']
        
        new_address = request.form['address']
        if new_address and new_address != user.address:
            user.address = new_address
            
        new_username = request.form['username']
        if new_username and new_username != user.username:
            user.username = new_username
        db.session.commit()
        flash('Profile updated successfully.', 'success')
        return redirect(url_for('profile.profile_page'))
        
    
    return render_template('profile.html', user = user)



@profile.route('/profile/upload_picture', methods=['POST'])
@login_required
def upload_profile_picture():
    user_id = session.get('user_id')
    
    if 'profile_picture' not in request.files:
        flash('No file part', 'error')
        return redirect(url_for('profile.profile_page'))
    
    file = request.files['profile_picture']
    
    if file.filename == '':
        flash('No selected file', 'error')
        return redirect(url_for('profile.profile_page'))
    
    filename = file.filename 
    file_path = os.path.join(Config.UPLOAD_FOLDER, filename).replace("\\", "/")
    
    file.save(file_path) 
    
    user = get_user_by_id(user_id)
    user.profile_picture = f'/static/img/profile_pics/{filename}'
    db.session.commit()
    
    flash('Profile picture updated successfully.', 'success')
    return redirect(url_for('profile.profile_page'))

@profile.route('/profile/change_password', methods=['POST'])
@login_required
def change_password():
    user_id = session.get('user_id')
    user = get_user_by_id(user_id)

    new_password = request.form.get('new_password')
    confirm_password = request.form.get('confirm_password')
    
    if new_password != confirm_password:
        flash('New password and confirmation do not match.', 'error')
        return redirect(url_for('profile.profile_page'))

    user.set_password(new_password)
    db.session.commit()

    flash('Password changed successfully!', 'success')
    return redirect(url_for('profile.profile_page'))


'''

1. Exemplo Vulnerável à CWE-22 (Path Traversal)
Neste exemplo, o código não valida adequadamente o nome do arquivo fornecido pelo usuário, permitindo a manipulação do caminho (path traversal). O usuário mal-intencionado pode enviar um caminho como ../../../../../etc/passwd e sobrescrever arquivos no sistema do servidor.

2. Exemplo Vulnerável à CWE-434 (Unrestricted File Upload)
Este exemplo também não valida corretamente o tipo de arquivo enviado. Isso permite que um invasor faça o upload de arquivos potencialmente maliciosos, como scripts executáveis, que poderiam comprometer o servidor.

'''
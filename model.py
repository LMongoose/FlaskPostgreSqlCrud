import database


def list_all(tablename):
    with database.Database() as db:
        if(tablename == "Animes"):
            table_animes = database.TableAnimes(db)
            results, columns = table_animes.list_all()

        elif(tablename == "Characters"):
            table_characters = database.TableCharacters(db)
            results, columns = table_characters.list_all()

        elif(tablename == "People"):
            table_people = database.TablePeople(db)
            results, columns = table_people.list_all()

        elif(tablename == "Users"):
            table_users = database.TableUsers(db)
            results, columns = table_users.list_all()

        elif(tablename == "Animeography"):
            table_animeography = database.TableAnimeography(db)
            results, columns = table_animeography.list_all()

        elif(tablename == "Staff"):
            table_staff = database.TableStaff(db)
            results, columns = table_staff.list_all()

        else:
            return None, None

    return results, columns

def select(tablename, selected_id, selected_id2):
    with database.Database() as db:
        if(tablename == "Animes"):
            table_animes = database.TableAnimes(db)
            result, columns = table_animes.select(selected_id)

        elif(tablename == "Characters"):
            table_characters = database.TableCharacters(db)
            result, columns = table_characters.select(selected_id)

        elif(tablename == "People"):
            table_people = database.TablePeople(db)
            result, columns = table_people.select(selected_id)

        elif(tablename == "Users"):
            table_users = database.TableUsers(db)
            result, columns = table_users.select(selected_id)

        elif(tablename == "Animeography"):
            table_animeography = database.TableAnimeography(db)
            result, columns = table_animeography.select(selected_id, selected_id2)

        elif(tablename == "Staff"):
            table_staff = database.TableStaff(db)
            result, columns = table_staff.select(selected_id, selected_id2)

        else:
            return None, None

    return result, columns

def insert(tablename, form):
    with database.Database() as db:
        if(tablename == "Animes"):
            table_animes = database.TableAnimes(db)
            if(form.get("id") is not None
                and form.get("title") is not None
                and form.get("type") is not None
                and form.get("synopsis") is not None
                and form.get("release_date") is not None    
                and form.get("episodes") is not None):
                    return table_animes.insert(
                        form.get("id"),
                        form.get("title"),
                        form.get("type"),
                        form.get("synopsis"),
                        form.get("release_date"),
                        form.get("episodes")
                    )

        elif(tablename == "Characters"):
            table_characters = database.TableCharacters(db)
            if(form.get("id") is not None
                and form.get("name") is not None
                and form.get("info") is not None):
                    return table_characters.insert(
                        form.get("id"),
                        form.get("name"),
                        form.get("info")
                    )

        elif(tablename == "People"):
            table_people = database.TablePeople(db)
            if(form.get("id") is not None
                and form.get("name") is not None
                and form.get("birthday") is not None):
                    return table_people.insert(
                        form.get("id"),
                        form.get("name"),
                        form.get("birthday")
                    )

        elif(tablename == "Users"):
            table_users = database.TableUsers(db)
            if(form.get("id") is not None
                and form.get("username") is not None
                and form.get("password") is not None
                and form.get("email") is not None):
                    return table_users.insert(
                        form.get("id"),
                        form.get("username"),
                        form.get("password"),
                        form.get("email")
                    )

        elif(tablename == "Animeography"):
            table_animeography = database.TableAnimeography(db)
            if(form.get("id_character") is not None
                and form.get("id_anime") is not None
                and form.get("role") is not None):
                    return table_animeography.insert(
                        form.get("id_anime"),
                        form.get("id_character"),
                        form.get("role")
                    )

        elif(tablename == "Staff"):
            table_staff = database.TableStaff(db)
            if(form.get("id_people") is not None
                and form.get("id_anime") is not None
                and form.get("role") is not None):
                    return table_staff.insert(
                        form.get("id_anime"),
                        form.get("id_people"),
                        form.get("role")
                    )

        else:
            return None

def update(tablename, selected_id, selected_id2, form):
    with database.Database() as db:
        if(tablename == "Animes"):
            table_animes = database.TableAnimes(db)
            if(form.get("id") is not None
                and form.get("title") is not None
                and form.get("type") is not None
                and form.get("synopsis") is not None
                and form.get("release_date") is not None    
                and form.get("episodes") is not None):
                    return table_animes.update(
                        form.get("id"),
                        form.get("title"),
                        form.get("type"),
                        form.get("synopsis"),
                        form.get("release_date"),
                        form.get("episodes")
                    )

        elif(tablename == "Characters"):
            table_characters = database.TableCharacters(db)
            if(form.get("id") is not None
                and form.get("name") is not None
                and form.get("info") is not None):
                    return table_characters.update(
                        form.get("id"),
                        form.get("name"),
                        form.get("info")
                    )

        elif(tablename == "People"):
            table_people = database.TablePeople(db)
            if(form.get("id") is not None
                and form.get("name") is not None
                and form.get("birthday") is not None):
                    return table_people.update(
                        form.get("id"),
                        form.get("name"),
                        form.get("birthday")
                    )

        elif(tablename == "Users"):
            table_users = database.TableUsers(db)
            if(form.get("id") is not None
                and form.get("username") is not None
                and form.get("password") is not None
                and form.get("email") is not None):
                    return table_users.update(
                        form.get("id"),
                        form.get("username"),
                        form.get("password"),
                        form.get("email")
                        )

        elif(tablename == "Animeography"):
            table_animeography = database.TableAnimeography(db)
            if(form.get("id_anime") is not None
                and form.get("id_character") is not None
                and form.get("role") is not None):
                    return table_animeography.update(
                        form.get("id_anime"),
                        form.get("id_character"),
                        form.get("role")
                    )

        elif(tablename == "Staff"):
            table_staff = database.TableStaff(db)
            if(form.get("id_anime") is not None
                and form.get("id_people") is not None
                and form.get("role") is not None):
                    return table_staff.update(
                        form.get("id_anime"),
                        form.get("id_people"),
                        form.get("role")
                    )

        else:
            return None

def delete(tablename, selected_id, selected_id2):
    with database.Database() as db:
        if(tablename == "Animes"):
            table_animes = database.TableAnimes(db)
            return table_animes.delete(selected_id)

        elif(tablename == "Characters"):
            table_characters = database.TableCharacters(db)
            return table_characters.delete(selected_id)

        elif(tablename == "People"):
            table_people = database.TablePeople(db)
            return table_people.delete(selected_id)

        elif(tablename == "Users"):
            table_users = database.TableUsers(db)
            return table_users.delete(selected_id)

        ## TODO: handle 2 fk cases
        elif(tablename == "Animeography"):
            table_animeography = database.TableAnimeography(db)
            return table_animeography.delete(selected_id, selected_id2)

        elif(tablename == "Staff"):
            table_staff = database.TableStaff(db)
            return table_staff.delete(selected_id, selected_id2)

        else:
            return None
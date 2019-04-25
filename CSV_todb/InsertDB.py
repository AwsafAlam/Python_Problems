# Amiangshu Sir


import pymysql.cursors



class ConnectorrDB:

  def __init__(self, host, user, password, db_name):
    self.connection=pymysql.connect(host=host,
                             user=user,
                             password=password,
                             db=db_name,
                             
                             cursorclass=pymysql.cursors.DictCursor)

    self.cursor=self.connection.cursor()



  def saveReviewer(self, gerrit_id, full_name, preferred_email, username, avatar):
      self.cursor.executemany("insert into people (gerrit_id,full_name,preferred_email,username,avatar) values(%s,%s,%s,%s,%s)",
                         (gerrit_id, full_name, preferred_email, username, avatar))
      self.connection.commit()

  def saveReviewRequestList(self,project_id, gerrit_id, gerrit_key, owner, owner_name,subject,status,project,branch,topic,
                            starred,last_updated_on,sort_key,insertions,deletions,owner_email,created):

      self.cursor.executemany("INSERT INTO requests "
						+ "(project_id,gerrit_id,gerrit_key,owner,owner_name,subject,"
                          + "status,project,branch,topic,starred,last_updated_on,sort_key,"
                          + "insertions,deletions,owner_email,created) VALUES"
						+ "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                         (project_id, gerrit_id, gerrit_key, owner, owner_name,subject,status,project,branch,topic,
                            starred,last_updated_on,sort_key,insertions,deletions,owner_email,created))
      self.connection.commit()


  def saveReviewRequestShortList(self,project_id,gerrit_id,gerrit_key,owner,sort_key):
      self.cursor.executemany("insert into requests_temp (project_id,gerrit_id,gerrit_key,owner,sort_key) values(%s,%s,%s,%s,%s)",
                         (project_id,gerrit_id,gerrit_key,owner,sort_key))
      self.connection.commit()

  def saveDetailsRequest( self,request_id,gerrit_id,project,branch,topic,change_id,subject,status,created,updated,
                          insertions,deletions,sort_key,mergeable,owner,number_patches,curent_patch_id):

      self.cursor.executemany("INSERT INTO request_detail ( request_id,gerrit_id,project,branch,topic,"
                          + "change_id,subject,status,created,updated,"
                          + "insertions,deletions,sort_key,mergeable,owner,"
                          + "number_patches,curent_patch_id)"
                          + " VALUES ( %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s)",
                         ( request_id,gerrit_id,project,branch,topic,change_id,subject,status,created,updated,
                          insertions,deletions,sort_key,mergeable,owner,number_patches,curent_patch_id))
      self.connection.commit()


  def patches(self,request_id,revision,patchset_number,comment_count,subject,message,checkout,cherrypick,
                          format,pull,author,committer,author_id,created,committed):

      self.cursor.executemany("INSERT INTO patches ( "+
                          "request_id,revision,patchset_number,"+
                          "comment_count,subject,message,checkout,cherrypick,"+
                          "format,pull,author,committer,author_id,created,committed)"+
                          " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                         (request_id,revision,patchset_number,comment_count,subject,message,checkout,cherrypick,
                          format,pull,author,committer,author_id,created,committed))
      self.connection.commit()


  def patchDetails(self,request_id,patchset_id,file_name,change_type,insertions,deletions):
      self.cursor.executemany("INSERT INTO patch_details "+
                          "(request_id,patchset_id,file_name,change_type,insertions,deletions)"+
                          " VALUES (%s, %s, %s, %s, %s, %s)",
                         (request_id,patchset_id,file_name,change_type,insertions,deletions))
      self.connection.commit()


  def ReviewComments(self,request_id,message_id,patchset_id,author,created,message):
      self.cursor.executemany("INSERT INTO review_comments "+
                          "(request_id,message_id,patchset_id,author,created,message)"+
                          " VALUES (%s,%s,%s,%s,%s,%s)",
                         (request_id,message_id,patchset_id,author,created,message))
      self.connection.commit()

  def Reviews(self,request_id,people_id,verified,reviewed,build):
      self.cursor.executemany("INSERT INTO reviews "+
                          "(request_id,people_id,verified,reviewed,build) "+
                          "VALUES (%s,%s,%s,%s,%s)",
                         (request_id,people_id,verified,reviewed,build))
      self.connection.commit()


  def inlineComments(self,comment_id,request_id,in_reply_to,patchset_id,file_name,line_number,author_id,written_on,status,side,
                     message,start_line,end_line,start_character,end_character):

      self.cursor.executemany("INSERT INTO inline_comments " +
                          "(comment_id,request_id,in_reply_to,patchset_id,file_name,"+
                          "line_number,author_id,written_on,status,side,"+
                          "message,start_line,end_line,start_character,end_character) VALUES " +
                          "(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)",
                         (comment_id,request_id,in_reply_to,patchset_id,file_name,line_number,author_id,
                           written_on,status,side,message,start_line,end_line,start_character,end_character))
      self.connection.commit()


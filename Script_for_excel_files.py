import requests

def Script_for_excel_files():

    excel_url_xwra_2015_a = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=187619&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_xwra_2015_a = requests.get(excel_url_xwra_2015_a)

    output = open('xwra_2015_a.xls', 'wb')
    output.write(response_xwra_2015_a.content)
    output.close()

    excel_url_meso_2015_a = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=187618&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_meso_2015_a = requests.get(excel_url_meso_2015_a)

    output = open('meso_2015_a.xls', 'wb')
    output.write(response_meso_2015_a.content)
    output.close()

    excel_url_xwra_2015_b = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=187604&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_xwra_2015_b = requests.get(excel_url_xwra_2015_a)

    output = open('xwra_2015_b.xls', 'wb')
    output.write(response_xwra_2015_b.content)
    output.close()

    excel_url_meso_2015_b = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=187603&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_meso_2015_b = requests.get(excel_url_xwra_2015_b)

    output = open('meso_2015_b.xls', 'wb')
    output.write(response_xwra_2015_b.content)
    output.close()

    excel_url_xwra_2015_c = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=187589&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_xwra_2015_c = requests.get(excel_url_xwra_2015_c)

    output = open('xwra_2015_c.xls', 'wb')
    output.write(response_xwra_2015_c.content)
    output.close()

    excel_url_meso_2015_c = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=187588&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_meso_2015_c = requests.get(excel_url_xwra_2015_c)

    output = open('meso_2015_c.xls', 'wb')
    output.write(response_xwra_2015_c.content)
    output.close()

    excel_url_xwra_2015_d = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=198754&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_xwra_2015_d = requests.get(excel_url_xwra_2015_d)

    output = open('xwra_2015_d.xls', 'wb')
    output.write(response_xwra_2015_d.content)
    output.close()

    excel_url_meso_2015_d = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=198755&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_meso_2015_d = requests.get(excel_url_xwra_2015_d)

    output = open('meso_2015_d.xls', 'wb')
    output.write(response_xwra_2015_d.content)
    output.close()

    excel_url_xwra_2013_a = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113888&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_xwra_2013_a = requests.get(excel_url_xwra_2013_a)

    output = open('xwra_2013_a.xls', 'wb')
    output.write(response_xwra_2013_a.content)
    output.close()

    excel_url_meso_2013_a = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113892&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_meso_2013_a = requests.get(excel_url_meso_2013_a)

    output = open('meso_2013_a.xls', 'wb')
    output.write(response_meso_2013_a.content)
    output.close()

    excel_url_xwra_2013_b = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113893&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_xwra_2013_b = requests.get(excel_url_xwra_2013_b)

    output = open('xwra_2013_b.xls', 'wb')
    output.write(response_xwra_2013_b.content)
    output.close()

    excel_url_meso_2013_b = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113895&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_meso_2013_b = requests.get(excel_url_meso_2013_b)

    output = open('meso_2013_b.xls', 'wb')
    output.write(response_meso_2013_b.content)
    output.close()

    excel_url_xwra_2013_c = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113902&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_xwra_2013_c = requests.get(excel_url_xwra_2013_c)

    output = open('xwra_2013_c.xls', 'wb')
    output.write(response_xwra_2013_c.content)
    output.close()

    excel_url_meso_2013_c = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113901&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_meso_2013_c = requests.get(excel_url_meso_2013_c)

    output = open('meso_2013_c.xls', 'wb')
    output.write(response_meso_2013_c.content)
    output.close()

    excel_url_xwra_2013_d = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113903&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_xwra_2013_d = requests.get(excel_url_xwra_2013_d)

    output = open('xwra_2013_d.xls', 'wb')
    output.write(response_xwra_2013_d.content)
    output.close()

    excel_url_meso_2013_d = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113905&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_meso_2013_d = requests.get(excel_url_meso_2013_d)

    output = open('meso_2013_d.xls', 'wb')
    output.write(response_meso_2013_d.content)
    output.close()

    excel_url_xwra_2014_a = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113910&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_xwra_2014_a = requests.get(excel_url_xwra_2014_a)

    output = open('xwra_2014_a.xls', 'wb')
    output.write(response_xwra_2014_a.content)
    output.close()

    excel_url_meso_2014_a = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113912&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_meso_2014_a = requests.get(excel_url_meso_2014_a)

    output = open('meso_2014_a.xls', 'wb')
    output.write(response_meso_2014_a.content)
    output.close()

    excel_url_xwra_2014_b = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113915&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_xwra_2014_b = requests.get(excel_url_xwra_2014_b)

    output = open('xwra_2014_b.xls', 'wb')
    output.write(response_xwra_2014_b.content)
    output.close()

    excel_url_meso_2014_b = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113917&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_meso_2014_b = requests.get(excel_url_meso_2014_b)

    output = open('meso_2014_b.xls', 'wb')
    output.write(response_meso_2014_b.content)
    output.close()

    excel_url_xwra_2014_c = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113921&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_xwra_2014_c = requests.get(excel_url_xwra_2014_c)

    output = open('xwra_2014_c.xls', 'wb')
    output.write(response_xwra_2014_c.content)
    output.close()

    excel_url_meso_2014_c = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113918&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_meso_2014_c = requests.get(excel_url_meso_2014_c)

    output = open('meso_2014_c.xls', 'wb')
    output.write(response_meso_2014_c.content)
    output.close()

    excel_url_xwra_2014_d = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113926&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_xwra_2014_d = requests.get(excel_url_xwra_2014_d)

    output = open('xwra_2014_d.xls', 'wb')
    output.write(response_xwra_2014_d.content)
    output.close()

    excel_url_meso_2014_d = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113925&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_meso_2014_d = requests.get(excel_url_meso_2014_d)

    output = open('meso_2014_d.xls', 'wb')
    output.write(response_meso_2014_d.content)
    output.close()

    excel_url_xwra_2012_a = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113868&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_xwra_2012_a = requests.get(excel_url_xwra_2012_a)

    output = open('xwra_2012_a.xls', 'wb')
    output.write(response_xwra_2012_a.content)
    output.close()

    excel_url_meso_2012_a = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113871&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_meso_2012_a = requests.get(excel_url_meso_2012_a)

    output = open('meso_2012_a.xls', 'wb')
    output.write(response_meso_2012_a.content)
    output.close()

    excel_url_xwra_2012_b = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113875&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_xwra_2012_b = requests.get(excel_url_xwra_2012_b)

    output = open('xwra_2012_b.xls', 'wb')
    output.write(response_xwra_2012_b.content)
    output.close()

    excel_url_meso_2012_b = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113877&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_meso_2012_b = requests.get(excel_url_meso_2012_b)

    output = open('meso_2012_b.xls', 'wb')
    output.write(response_meso_2012_b.content)
    output.close()

    excel_url_xwra_2012_c = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113881&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_xwra_2012_c = requests.get(excel_url_xwra_2012_c)

    output = open('xwra_2012_c.xls', 'wb')
    output.write(response_xwra_2012_c.content)
    output.close()

    excel_url_meso_2012_c = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113882&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_meso_2012_c = requests.get(excel_url_meso_2012_c)

    output = open('meso_2012_c.xls', 'wb')
    output.write(response_meso_2012_c.content)
    output.close()

    excel_url_xwra_2012_d = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113885&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_xwra_2012_d = requests.get(excel_url_xwra_2012_d)

    output = open('xwra_2012_d.xls', 'wb')
    output.write(response_xwra_2012_d.content)
    output.close()

    excel_url_meso_2012_d = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113886&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_meso_2012_d = requests.get(excel_url_meso_2012_d)

    output = open('meso_2012_d.xls', 'wb')
    output.write(response_meso_2012_d.content)
    output.close()

    excel_url_xwra_2011_a = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113851&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_xwra_2011_a = requests.get(excel_url_xwra_2011_a)

    output = open('xwra_2011_a.xls', 'wb')
    output.write(response_xwra_2011_a.content)
    output.close()

    excel_url_meso_2011_a = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113852&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_meso_2011_a = requests.get(excel_url_meso_2011_a)

    output = open('meso_2011_a.xls', 'wb')
    output.write(response_meso_2011_a.content)
    output.close()

    excel_url_xwra_2011_b = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113853&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_xwra_2011_b = requests.get(excel_url_xwra_2011_b)

    output = open('xwra_2011_b.xls', 'wb')
    output.write(response_xwra_2011_b.content)
    output.close()

    excel_url_meso_2011_b = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113856&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_meso_2011_b = requests.get(excel_url_meso_2011_b)

    output = open('meso_2011_b.xls', 'wb')
    output.write(response_meso_2011_b.content)
    output.close()

    excel_url_xwra_2011_c = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113858&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_xwra_2011_c = requests.get(excel_url_xwra_2011_c)

    output = open('xwra_2011_c.xls', 'wb')
    output.write(response_xwra_2011_c.content)
    output.close()

    excel_url_meso_2011_c = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113861&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_meso_2011_c = requests.get(excel_url_meso_2011_c)

    output = open('meso_2011_c.xls', 'wb')
    output.write(response_meso_2011_c.content)
    output.close()

    excel_url_xwra_2011_d = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113866&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_xwra_2011_d = requests.get(excel_url_xwra_2011_d)

    output = open('xwra_2011_d.xls', 'wb')
    output.write(response_xwra_2011_d.content)
    output.close()

    excel_url_meso_2011_d = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113865&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
    response_meso_2011_d = requests.get(excel_url_meso_2011_d)

    output = open('meso_2011_d.xls', 'wb')
    output.write(response_meso_2013_d.content)
    output.close()


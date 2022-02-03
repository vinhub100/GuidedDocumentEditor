subhead_text = '<div style = "text-align: center;margin: 10px 0px;display: flex;" >\
    <textarea class = "form-control a_subhead  a_item" id = "" rows = "1"\
            style = "width:97%" placeholder = "Sub Heading" >{value}</textarea >\
        <p class = "item_cancel_btn" >×</p >\
    </div >\
    <div class = "add_btn_cnt" >\
       <div style = "width: 100%;position: absolute;" >\
           <hr style = "margin-bottom: -15px;" >\
            <button class = "float-right round_btn" > +</button>\
        </div >\
    </div >'


img_text = ' <div style = "text-align: center;margin: 10px 0px;display: flex;" >\
                <div style = "width: 97%;" >\
                    <img class = "a_image a_item" width = "800px" src = "{value}" >\
                </div >\
                <p class = "item_cancel_btn" >×</p >\
            </div>\
            <div class="add_btn_cnt">\
                <div style="width: 100%;position: absolute;">\
                    <hr style="margin-bottom: -15px;">\
                    <button class="float-right round_btn">+</button>\
                </div>\
            </div>'

para_text = '<div style = "text-align: center;margin: 10px 0px;display: flex;" >\
        <textarea class = "form-control a_para  a_item" id = "" rows="3"\
            style = "width:97%" placeholder = "Article Paragragh">{value}</textarea>\
        <p class = "item_cancel_btn" >×</p >\
    </div >\
    <div class = "add_btn_cnt" >\
       <div style = "width: 100%;position: absolute;" >\
           <hr style = "margin-bottom: -15px;" >\
            <button class = "float-right round_btn" > +</button>\
        </div >\
    </div >'


list_text = '<div style = "text-align: center;margin: 10px 0px;display: flex;" >\
        <textarea class = "form-control a_list a_item" id = "" rows="5"\
            style = "width:97%" placeholder = "Enter Each List Item in New Line">{value}</textarea>\
        <p class = "item_cancel_btn" >×</p >\
    </div >\
    <div class = "add_btn_cnt" >\
       <div style = "width: 100%;position: absolute;" >\
           <hr style = "margin-bottom: -15px;" >\
            <button class = "float-right round_btn" > +</button>\
        </div >\
    </div >'


yt_text = '<div style = "text-align: center;margin: 10px 0px;display: flex;" >\
        <textarea class = "form-control a_yt a_item" id = "" rows="1"\
            style = "width:97%" placeholder = "Enter Youtube Video ID">{value}</textarea>\
        <p class = "item_cancel_btn" >×</p >\
    </div >\
    <div class = "add_btn_cnt" >\
       <div style = "width: 100%;position: absolute;" >\
           <hr style = "margin-bottom: -15px;" >\
            <button class = "float-right round_btn" > +</button>\
        </div >\
    </div >'


def render_body(bdy):
    html = ''
    for i in bdy:
        item = bdy[i]
        typ = item['type']
        if typ == 'PARA':
            html += '<p>' + item['value'] + '</p>'
        elif typ == 'SUBHEAD':
            html += '<h4>' + item['value'] + '</h4>'
        elif typ == 'IMAGE':
            html += '<img src="' + item['value'] + '"  class="img-fluid">'
        elif typ == 'LIST':
            lit = item['value'].split('⬜')
            li = ''
            for l in lit:
                li += '<li>' + l + '</li>'
            html += '<ul>' + li + '</ul>'
        elif typ == 'YTVDO':
            html += '<div class="iframe-container"><iframe class="responsive-iframe" src="https://www.youtube.com/embed/' + \
                item['value'] + '" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>'
        else:
            pass
    return html


def update_body(body):
    form_body = ''
    for i in body:
        item = body[i]
        typ = item['type']
        if typ == 'PARA':
            form_body += para_text.format(value=item['value'])
        elif typ == 'SUBHEAD':
            form_body += subhead_text.format(value=item['value'])
        elif typ == 'LIST':
            lst = item['value'].replace('⬜', '\n')
            form_body += list_text.format(value=lst)
        elif typ == 'IMAGE':
            form_body += img_text.format(value=item['value'])
        elif typ == 'YTVDO':
            form_body += yt_text.format(value=item['value'])
        else:
            pass
    return form_body

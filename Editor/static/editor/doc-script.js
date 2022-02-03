let subhead_text = `
                                <div style="text-align: center;margin: 10px 0px;display: flex;">
                                    <textarea class="form-control a_subhead  a_item" id="" rows="1"
                                        style="width:97%" placeholder="Sub Heading ( Do not Use Double Quote )"></textarea>
                                    <p class="item_cancel_btn">×</p>
                                </div>
                                <div class="add_btn_cnt">
                                    <div style="width: 100%;position: absolute;">
                                        <hr style="margin-bottom: -15px;">
                                        <button class="float-right round_btn">+</button>
                                    </div>
                                </div>
`;


let img_text = `
                                <div style="text-align: center;margin: 10px 0px;display: flex;">
                                    <div style="width: 97%;">
                                        <img class="a_image a_item" width="800px" src="/static/editor/add_image_placeholder.svg">
                                    </div>
                                    <p class="item_cancel_btn">×</p>
                                </div>
                                <div class="add_btn_cnt">
                                    <div style="width: 100%;position: absolute;">
                                        <hr style="margin-bottom: -15px;">
                                        <button class="float-right round_btn">+</button>
                                    </div>
                                </div>
`;

let para_text = `
                                <div style="text-align: center;margin: 10px 0px;display: flex;">
                                    <textarea class="form-control a_para a_item auto_resize" id="" rows="3"
                                        style="width:97%" placeholder="Article Paragragh ( Do not Use Double Quote )"></textarea>
                                    <p class="item_cancel_btn">×</p>
                                </div>
                                <div class="add_btn_cnt">
                                    <div style="width: 100%;position: absolute;">
                                        <hr style="margin-bottom: -15px;">
                                        <button class="float-right round_btn">+</button>
                                    </div>
                                </div>
`;


let list_text = `
                                <div style="text-align: center;margin: 10px 0px;display: flex;">
                                    <textarea class="form-control a_list a_item auto_resize" id="" rows="5"
                                        style="width:97%" placeholder="Enter Each List Item in New Line. ( Do not Use Double Quote )"></textarea>
                                    <p class="item_cancel_btn">×</p>
                                </div>
                                <div class="add_btn_cnt">
                                    <div style="width: 100%;position: absolute;">
                                        <hr style="margin-bottom: -15px;">
                                        <button class="float-right round_btn">+</button>
                                    </div>
                                </div>
`;


let yt_text = `
                                <div style="text-align: center;margin: 10px 0px;display: flex;">
                                    <textarea class="form-control a_yt a_item" id="" rows="1"
                                        style="width:97%" placeholder="Enter Youtube Video ID"></textarea>
                                    <p class="item_cancel_btn">×</p>
                                </div>
                                <div class="add_btn_cnt">
                                    <div style="width: 100%;position: absolute;">
                                        <hr style="margin-bottom: -15px;">
                                        <button class="float-right round_btn">+</button>
                                    </div>
                                </div>
`;

let ason = '';

let option_modal_target = null;

let image_store_target = null;

$(document).ready(function() {



    $('#article_form').on('click', '.item_cancel_btn', (ev) => {
        ev.preventDefault();
        ev.target.parentElement.nextElementSibling.remove();
        ev.target.parentElement.remove();
    });

    $('.option_modal_close').click((ev) => {
        option_modal_target = null;
        $('.option_modal_container').hide();
    });

    $('#article_form').on('click', '.round_btn', (ev) => {
        ev.preventDefault();
        option_modal_target = ev.target.parentElement.parentElement;
        $('.option_modal_container').show();
    });

    $('#add_subhead').click((ev) => {
        ev.preventDefault();
        $(subhead_text).insertAfter(option_modal_target);
        $('.option_modal_container').hide();
    });

    $('#add_para').click((ev) => {
        ev.preventDefault();
        $(para_text).insertAfter(option_modal_target);
        $('.option_modal_container').hide();
    });

    $('#add_list').click((ev) => {
        ev.preventDefault();
        $(list_text).insertAfter(option_modal_target);
        $('.option_modal_container').hide();
    });

    $('#add_img').click((ev) => {
        ev.preventDefault();
        $(img_text).insertAfter(option_modal_target);
        $('.option_modal_container').hide();
    });

    $('#add_yt').click((ev) => {
        ev.preventDefault();
        $(yt_text).insertAfter(option_modal_target);
        $('.option_modal_container').hide();
    });


    function prepare_ason() {

        ason = '';

        item = $('.a_item');

        for (i = 0; i < item.length; i++) {
            cls = item[i].className;
            vl = '"' + i + '"';
            // console.log(vl);
            if (cls.includes('a_image')) {
                i_sr = new URL(item[i].src);
                ason += vl + ':{"type":"IMAGE","value":"' + i_sr.pathname + '"}';
            } else if (cls.includes('a_para')) {
                ason += vl + ':{"type":"PARA","value":"' + item[i].value.replace(/\n/g, " ") + '"}';
            } else if (cls.includes('a_subhead')) {
                ason += vl + ':{"type":"SUBHEAD","value":"' + item[i].value.replace(/\n/g, " ") + '"}';
            } else if (cls.includes('a_list')) {
                ason += vl + ':{"type":"LIST","value":"' + item[i].value.replace(/\n/g, "⬜") + '"}';
            } else if (cls.includes('a_yt')) {
                ason += vl + ':{"type":"YTVDO","value":"' + item[i].value + '"}';
            }

            if (i != item.length - 1) {
                ason += ',';
            }

        }

        ason = '{' + ason + '}';


    }

    function send_to_server(ev, artitype) {
        prepare_ason();

        heading = $('#article_heading').val();
        discription = $('#article_discription').val();
        dp = $('#article_dp').attr('src');
        console.log(dp)

        data = {
            'heading': heading,
            'discription': discription,
            'a_type': artitype,
            'dp': dp,
            'body': ason
        };

        fetch(document.location.pathname, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }).then((responce) => {
            if (responce.status == '200') {
                window.location = "/editor/"
            }
        });
        console.log(document.location)
        ason = "";
    }

    $('#a_post').click((ev) => {
        send_to_server(ev, 'P');
    });

    $('#a_draft').click((ev) => {
        send_to_server(ev, 'D');
    });

    $('#a_preview').click((ev) => {
        prepare_ason();
        let jyson = JSON.parse(ason);
        let jyson_len = Object.keys(jyson).length;
        let content = '';

        $('#arti_preview').html(" ");

        heading = $('#article_heading').val();
        content += '<h1>' + heading + '</h1>';
        discription = $('#article_discription').val();
        content += '<p class="discription">' + discription + '</p><hr>';

        for (i = 0; i < jyson_len; i++) {
            typ = jyson[i]['type'];
            valu = jyson[i]['value'];

            if (typ == 'SUBHEAD') {
                content += '<h4>' + valu + '</h4>';
            } else if (typ == 'PARA') {
                content += '<p>' + valu + '</p>';
            } else if (typ == 'LIST') {
                vl = valu.split("⬜");
                lis = "";
                for (j = 0; j < vl.length; j++) {
                    lis += '<li>' + vl[j] + '</li>';
                }
                content += '<ul>' + lis + '</ul>';
            } else if (typ == 'IMAGE') {
                content += '<img src="' + valu + '" width="800px" style="display:block;margin-left: auto;margin-right: auto;padding:30px">';
            } else if (typ == 'YTVDO') {
                content += '<iframe style="display:block;margin-left: auto;margin-right: auto;padding:30px" width="800" height="450" src="https://www.youtube.com/embed/' + valu + '" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
            } else {

            }

        }

        $('#arti_preview').html(content);

        $('.a_main_container').hide();
        $('.priview_modal_container').fadeIn();
        ason = "";
    });

    $('#priview_modal_close').click((ev) => {
        $('.priview_modal_container').hide();
        $('.a_main_container').show();
    });

    $('#imagestore_modal_close').click((ev) => {
        $('.imagestore_container').hide();
        image_store_target = null;
    });

    $('#article_form').on('click', '.a_image', (ev) => {
        image_store_target = ev.target;
        $('.imagestore_container').show();
    });


    $('#imagestore_select').click((ev) => {
        ur = document.getElementById('imagestore').contentWindow.document.querySelector('#selected_image_disp').innerText;
        image_store_target.src = ur;
        $('.imagestore_container').hide();
        image_store_target = null;
    });


    $('.im_card').click((ev) => {
        im_lnk = new URL(ev.target.src);
        $('#selected_image_disp').text(im_lnk.pathname);
    });

    $('#article_form').on('input', '.auto_resize', (ev) => {
        tx = ev.target.value;
        nl = 1;
        for (i = 0; i < tx.length; i++) {
            if (tx[i] == '\n') {
                nl++;
            }
        }
        $(ev.target).attr('rows', nl);
    });


});
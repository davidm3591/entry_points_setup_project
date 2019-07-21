import os
import xlsxwriter
import sys
import shutil
from xlsxwriter.utility import xl_range, xl_rowcol_to_cell
import re
########################################################################
# Extraction Tool
# Edgenuity, Inc.
########################################################################
# Sub-module
# Performs (mostly) output of PowerPoint data collected and processed
# by extraction_pptx.py
# - 07/04/2019 drm
########################################################################


def brk_if():
    test_stop = input("\nContinue loop (y/n)? ")
    test_stop = test_stop.lower()
    if test_stop == 'y':
        pass
    else:
        sys.exit(None)


# slide_break is format only -- delete at final build
slide_break = 2 * ("================================")
########################################################################


def app_kill():
    sys.exit(None)


fname = re.compile(r'\d+-\d{2}-\d{2}-\d{2}-\d{2}-')


def excel_data_out(vid_qa_sheet_data, ext_sheet_data,
                   vo_data_summary, f_name, vocab_words,
                   frame, time_key_list, frame_times,
                   basic_info, basic_vid_qa):

    activity_time_list_5 = []
    activity_time_list_10 = []
    activity_time_list_15 = []
    activity_time_list_20 = []
    activity_time_list_25 = []
    activity_time_list_30 = []
    activity_time_list_35 = []
    activity_time_list_40 = []
    activity_time_list_45 = []
    activity_time_list_50 = []
    activity_time_list_55 = []
    activity_time_list_60 = []
    activity_time_list_65 = []
    activity_time_list_70 = []

    f_path = 'C:\\e2020_tool_data\\output\\'

    # Build the workbook and worksheets
    workbook = xlsxwriter.Workbook(f_path + f_name + '.xlsx')
    worksheet1 = workbook.add_worksheet('Extraction Sheet')
    worksheet2 = workbook.add_worksheet('Video QA')
    worksheet3 = workbook.add_worksheet(f'{f_name}-VO')
    worksheet4 = workbook.add_worksheet(f'{f_name}-Vocab')

    heading_format = workbook.add_format(
        {'bottom': 1, 'bold': True, 'indent': 1})

    content_line = workbook.add_format(
        {'bottom': 1, 'bottom_color': '#adb3bc', 'align': 'center', 'indent': 1})

    ext_sht_content_line = workbook.add_format(
        {'valign': 'top', 'bottom': 1, 'bottom_color': '#adb3bc', 'align': 'center', 'indent': 1, 'text_wrap': True})

    ext_sht_video_line = workbook.add_format(
        {'bg_color': '#f9ff33', 'valign': 'top', 'bottom': 1, 'bottom_color': '#adb3bc', 'align': 'center', 'indent': 1, 'text_wrap': True})

    title_form = workbook.add_format(
        {'bold': True, 'font_size': 14})

    intro_text = workbook.add_format({'bold': True, 'indent': 2})

    act_time_text = workbook.add_format({'bold': True})

    vid_qa_col_1_3 = workbook.add_format(
        {'bottom': 1, 'bottom_color': '#adb3bc', 'align': 'center'})

    # Define the background colors for conditional formatting vid qa
    vid_qa_valid_1 = workbook.add_format({'bg_color': '#05C713',
                                          'font_color': '#000000'})
    vid_qa_valid_2 = workbook.add_format({'bg_color': '#FADD06',
                                          'font_color': '#000000'})
    vid_qa_valid_3 = workbook.add_format({'bg_color': '#D75959',
                                          'font_color': '#000000'})

    vo_num_align = workbook.add_format(
        {
            'bottom': 1, 'bottom_color': '#adb3bc',
            'top': 1, 'top_color': '#adb3bc',
            'align': 'left', 'indent': 2, 'align': 'vcenter'
        }
    )
    vo_content_line = workbook.add_format(
        {
            'bottom': 1, 'bottom_color': '#adb3bc',
            'top': 1, 'top_color': '#adb3bc',
            'align': 'left', 'indent': 2, 'align': 'vcenter',
            'text_wrap': True
        }
    )

    vo_content_filename = workbook.add_format(
        {
            'bottom': 1, 'bottom_color': '#adb3bc',
            'top': 1, 'top_color': '#adb3bc',
            'align': 'left', 'indent': 2, 'align': 'vcenter'
        }
    )

    worksheet1.hide_gridlines(2)
    worksheet2.hide_gridlines(2)
    worksheet2.set_landscape
    worksheet3.hide_gridlines(2)
    worksheet4.hide_gridlines(2)

    worksheet2.set_column('A:A', 12.43)
    worksheet2.set_column('B:B', 7)
    worksheet2.set_column('C:C', 7.4)
    worksheet2.set_column('D:D', 31)
    worksheet2.set_column('E:E', 6.89)
    worksheet2.set_column('F:F', 11.86)
    worksheet2.set_column('G:G', 9.5)
    worksheet2.set_column('H:H', 11.5)
    worksheet2.set_column('I:I', 17)

    worksheet3.set_column('A:A', 5)
    worksheet3.set_column('B:B', 54)
    worksheet3.set_column('C:C', 28)

    worksheet4.set_column('A:A', 18)
    worksheet4.set_column('B:B', 25)
    worksheet4.set_column('C:C', 38)
    worksheet4.set_column('D:D', 30)


# ################### Build the Extraction Worksheet  ##################
    # Build doc title
    extraction_title = f'{f_name}-Extraction Sheet'
    row = 0
    col = 0
    worksheet1.write(row, col, extraction_title, title_form)
    extraction_author = 'Author:'
    extraction_version = 'Version #:'

    row = 2
    col = 0
    for info_basic in basic_info:
        info_basic = info_basic.replace('\t', ' ')
        worksheet1.write(row, col, info_basic, act_time_text)
        # col += 1
        row += 1
    worksheet1.write(row, col, extraction_author, act_time_text)
    row += 1
    worksheet1.write(row, col, extraction_version, act_time_text)

    # Header data for the extraction sheet worksheet
    extract_headers = (
        'Activity Name', 'Activity Type', 'Frame Chain',
        'Frame', 'Slide Title     ', 'Slide #',
        'Type      ',
        'Slide Layout     ', 'Filename (frame reference-type) ',
        'Actual Est Time', 'Actual Time',
        'Comments',
    )

    # Build the header for the Extraction worksheet
    row = 9
    col = 0
    for extract_header in (extract_headers):
        # Set the column width based on string length + 2
        worksheet1.set_column('{0}:{0}'.format(
            chr(col + ord('A'))), len(str(extract_header)) + 2)
        worksheet1.write(row, col, extract_header, heading_format)
        col += 1

    row = 10
    col = 0
    for ext_data in ext_sheet_data:
        col = 0
        vid_row = False
        if 'video' in ext_data:
            vid_row = True
        else:
            vid_row = False
        for elem in ext_data:
            if vid_row is True:
                worksheet1.write(row, col, elem, ext_sht_video_line)
                worksheet1.write(row, 9, ' ', ext_sht_content_line)
                worksheet1.write(row, 10, ' ', ext_sht_content_line)
                worksheet1.write(row, 11, ' ', ext_sht_content_line)
                col += 1
            elif vid_row is False:
                worksheet1.write(row, col, elem, ext_sht_content_line)
                col += 1
        row += 1


# #################### Build the Video QA Worksheet  ###################
    # Build doc title
    vid_qa_title = f'{f_name}-Video QA Worksheet (Print: Landscape)'
    row = 0
    col = 0
    worksheet2.write(row, col, vid_qa_title, title_form)

    # Build intro info for the Video QA worksheet
    video_qa_filmer = 'Filmer Name:'
    video_qa_person = 'QAer Name:'

    row = 2
    col = 0
    for qa_vid_basic in (basic_vid_qa):
        qa_vid_basic = qa_vid_basic.replace('\t', ' ')
        worksheet2.write(row, col, qa_vid_basic, act_time_text)
        row += 1
    worksheet2.write(row, col, video_qa_filmer, act_time_text)
    row += 1
    worksheet2.write(row, col, video_qa_person, act_time_text)

    # Header data for the Video QA worksheet
    vid_qa_headers = (
        'Frame Chain', 'Frame', 'Slide #',
        'Filename (frame reference-type)', 'Type', 'Date Filmed',
        'Length', 'Status', 'Comments',
    )

    # Build the Video QA header for the extraction worksheet
    row = 10
    col = 0
    for vid_qa_header in (vid_qa_headers):
        worksheet2.write(row, col, vid_qa_header, heading_format)
        col += 1

    # Output the video qa data to the Video QA worksheet
    vid_qa_count = 0  # track number of rows for dd and cond format
    col = 0
    row = 11
    for vid_qa in vid_qa_sheet_data:
        col = 0
        # Make sure video row also has a filename in it
        chk_file = fname.findall(str(vid_qa))
        if chk_file:
            for elem in vid_qa:
                worksheet2.write(row, col, elem, content_line)
                col += 1
            row += 1
        else:
            pass
        vid_qa_count += 1

    # Code to create DDs based on vid_qa_count (iterations)
    # Row always starts at 11
    worksheet2.data_validation(11, 7, vid_qa_count + 10, 7, {'validate': 'list',
                                                             'source': ['RFP',
                                                                        '2nd Review',
                                                                        'RESHOOT']})

    # Write a conditional format over range defined by vid_qa_count.
    worksheet2.conditional_format(11, 7, vid_qa_count + 10, 7, {'type': 'cell',
                                                                'criteria': 'equal to',
                                                                'value': '"RFP"',
                                                                'format': vid_qa_valid_1})

    # Write another conditional format over the same range.
    worksheet2.conditional_format(11, 7, vid_qa_count + 10, 7, {'type': 'cell',
                                                                'criteria': 'equal to',
                                                                'value': '"2nd Review"',
                                                                'format': vid_qa_valid_2})

    # Write another conditional format over the same range.
    worksheet2.conditional_format(11, 7, vid_qa_count + 10, 7, {'type': 'cell',
                                                                'criteria': 'equal to',
                                                                'value': '"RESHOOT"',
                                                                'format': vid_qa_valid_3})

    # Add legend for RFP, 2nd Review, and RESHOOT in H:H at vid_qa_count + 3
    # row starts at 3 more than (vid_qa_count + 11)
    worksheet2.write(vid_qa_count + 13, 7, 'RFP', vid_qa_valid_1)
    worksheet2.write(vid_qa_count + 14, 7, '2nd Review', vid_qa_valid_2)
    worksheet2.write(vid_qa_count + 15, 7, 'RESHOOT', vid_qa_valid_3)

    # Add Total time to col G:G
    worksheet2.write(vid_qa_count + 11, 6, 'Total Time', act_time_text)
    # Format total time cell
    vid_qa_time = workbook.add_format()
    vid_qa_time.set_num_format('hh:mm:ss')
    # Define cell range for total time SUM formula
    cell_range = xl_range(11, 6, vid_qa_count + 10, 6)
    formula = '=SUM(%s)' % cell_range
    # Output the formula and format to the total time cell
    worksheet2.write(vid_qa_count + 12, 6, formula, vid_qa_time)

    # Create textbox for Video QA worksheet
    text = """REVIEW CRITERIA
    Speaker Rate/Flow:  Does the teacher speak in a natural pace that is appropriate for video?
    Speaker Presentation: Does the teacher make adequate use of the pen tool to draw students attention in to the lesson?
    Lesson flow: Do the ideas transition seamlessly from one to the next?  Are the Lesson Questions supported with
    \tappropriate detail that reinforce the big idea?
    Mistakes/Misspeaks: Are there any misspeaks or mistakes that will lead to student's learning inaccurate information?
    Content errors on slides or in spoken information:  Does the information on the slide match what the teacher is saying?
    Production Issues: Are there any issues with the quality of the video regarding audio or video,  clothing selection, etc.?
    """
    options = {
        'width': 785,
        'height': 165,
        'text_wrap': False,
        'align': {'vertical': 'top',
                  'horizontal': 'left'
                  },
    }

    worksheet2.insert_textbox('F2', text, options)

# #################### Build the VO Data Worksheet  ####################
# Output the vo data to the vo worksheet
    vo_doc_title = f'{f_name}-VO Worksheet (Print: Portrait)'
    col = 0
    row = 0
    worksheet3.write(row, col, vo_doc_title, title_form)
    col = 0
    row = 2
    i = 0
    for vo_f, vo_dat in vo_data_summary:
        col = 1
        worksheet3.write(row, col, vo_dat, vo_content_line)
        col = 2
        worksheet3.write(row, col, vo_f, vo_content_filename)
        col = 0
        i += 1
        worksheet3.write(row, col, i, vo_num_align)
        row += 1

# #############  Build the Vocab Word/Definition Worksheet #############
    first_frame = frame[0]
    m = first_frame[0:4]
    u = first_frame[4:7]
    l = first_frame[7:10]
    pre_num = f'{m}{u}{l}'

    vocab_doc_title = (f'{f_name}-Vocab Worksheet (Print: Landscape)')
    col = 0
    row = 0
    worksheet4.write(row, col, vocab_doc_title, title_form)

    col = 0
    row = 2
    for vocab_word, definition in vocab_words.items():
        col = 0
        worksheet4.write(
            row, col, f"{(vocab_word.rstrip()).title()}", vo_num_align)
        col += 1
        worksheet4.write(row, col, f"{pre_num}-{vocab_word}", vo_num_align)
        col += 1
        worksheet4.write(
            row, col, f"{(definition.lstrip()).capitalize()}", vo_content_line)
        col += 1
        worksheet4.write(
            row, col, f"{pre_num}-{vocab_word.rstrip()}-def", vo_num_align)
        row += 1


# #######  Build activity time totals ########
    t_k_count = 0
    for t_k in time_key_list:
        t_k_count += 1

    frame_key_time = {i: [j] for i, j in zip(time_key_list, frame_times)}

    # Activity 05
    for k, v in frame_key_time.items():
        if "->05" in k:
            activity_time_list_5.append(v)
    # Unpack list of activity_time_list_5 (list of lists)
    new_activity_list_5 = []
    for unpack_times in activity_time_list_5:
        new_activity_list_5.append(*unpack_times)
    est_time_05 = tuple(new_activity_list_5)
    total_05_time = 0
    for time_05 in est_time_05:
        sum_times_05 = float(time_05)
        total_05_time += sum_times_05

    # Activity 10
    for k, v in frame_key_time.items():
        if "->10" in k:
            activity_time_list_10.append(v)
    # Unpack list of activity_time_list_10 (list of lists)
    new_activity_list_10 = []
    for unpack_times in activity_time_list_10:
        new_activity_list_10.append(*unpack_times)
    est_time_10 = tuple(new_activity_list_10)
    total_10_time = 0
    for time_10 in est_time_10:
        sum_times_10 = float(time_10)
        total_10_time += sum_times_10

    # Activity 15
    for k, v in frame_key_time.items():
        if "->15" in k:
            activity_time_list_15.append(v)
    # Unpack list of activity_time_list_15 (list of lists)
    new_activity_list_15 = []
    for unpack_times in activity_time_list_15:
        new_activity_list_15.append(*unpack_times)
    est_time_15 = tuple(new_activity_list_15)
    total_15_time = 0
    for time_15 in est_time_15:
        sum_times_15 = float(time_15)
        total_15_time += sum_times_15

    # Activity 20
    for k, v in frame_key_time.items():
        if "->20" in k:
            activity_time_list_20.append(v)
    # Unpack list of activity_time_list_20 (list of lists)
    new_activity_list_20 = []
    for unpack_times in activity_time_list_20:
        new_activity_list_20.append(*unpack_times)
    est_time_20 = tuple(new_activity_list_20)
    total_20_time = 0
    for time_20 in est_time_20:
        sum_times_20 = float(time_20)
        total_20_time += sum_times_20

    # Activity 25
    for k, v in frame_key_time.items():
        if "->25" in k:
            activity_time_list_25.append(v)
    # Unpack list of activity_time_list_25 (list of lists)
    new_activity_list_25 = []
    for unpack_times in activity_time_list_25:
        new_activity_list_25.append(*unpack_times)
    est_time_25 = tuple(new_activity_list_25)
    total_25_time = 0
    for time_25 in est_time_25:
        sum_times_25 = float(time_25)
        total_25_time += sum_times_25

    # Activity 30
    for k, v in frame_key_time.items():
        if "->30" in k:
            activity_time_list_30.append(v)
    # Unpack list of activity_time_list_30 (list of lists)
    new_activity_list_30 = []
    for unpack_times in activity_time_list_30:
        new_activity_list_30.append(*unpack_times)
    est_time_30 = tuple(new_activity_list_30)
    total_30_time = 0
    for time_30 in est_time_30:
        sum_times_30 = float(time_30)
        total_30_time += sum_times_30

    # Activity 35
    for k, v in frame_key_time.items():
        if "->35" in k:
            activity_time_list_35.append(v)
    # Unpack list of activity_time_list_35 (list of lists)
    new_activity_list_35 = []
    for unpack_times in activity_time_list_35:
        new_activity_list_35.append(*unpack_times)
    est_time_35 = tuple(new_activity_list_35)
    total_35_time = 0
    for time_35 in est_time_35:
        sum_times_35 = float(time_35)
        total_35_time += sum_times_35

    # Activity 40
    for k, v in frame_key_time.items():
        if "->40" in k:
            activity_time_list_40.append(v)
    # Unpack list of activity_time_list_40 (list of lists)
    new_activity_list_40 = []
    for unpack_times in activity_time_list_40:
        new_activity_list_40.append(*unpack_times)
    est_time_40 = tuple(new_activity_list_40)
    total_40_time = 0
    for time_40 in est_time_40:
        sum_times_40 = float(time_40)
        total_40_time += sum_times_40

    # Activity 45
    for k, v in frame_key_time.items():
        if "->45" in k:
            activity_time_list_45.append(v)
    # Unpack list of activity_time_list_45 (list of lists)
    new_activity_list_45 = []
    for unpack_times in activity_time_list_45:
        new_activity_list_45.append(*unpack_times)
    est_time_45 = tuple(new_activity_list_45)
    total_45_time = 0
    for time_45 in est_time_45:
        sum_times_45 = float(time_45)
        total_45_time += sum_times_45

    # Activity 50
    for k, v in frame_key_time.items():
        if "->50" in k:
            activity_time_list_50.append(v)
    # Unpack list of activity_time_list_50 (list of lists)
    new_activity_list_50 = []
    for unpack_times in activity_time_list_50:
        new_activity_list_50.append(*unpack_times)
    est_time_50 = tuple(new_activity_list_50)
    total_50_time = 0
    for time_50 in est_time_50:
        sum_times_50 = float(time_50)
        total_50_time += sum_times_50

    # Activity 55
    for k, v in frame_key_time.items():
        if "->55" in k:
            activity_time_list_55.append(v)
    # Unpack list of activity_time_list_55 (list of lists)
    new_activity_list_55 = []
    for unpack_times in activity_time_list_55:
        new_activity_list_55.append(*unpack_times)
    est_time_55 = tuple(new_activity_list_55)
    total_55_time = 0
    for time_55 in est_time_55:
        sum_times_55 = float(time_55)
        total_55_time += sum_times_55

    # Activity 60
    for k, v in frame_key_time.items():
        if "->60" in k:
            activity_time_list_60.append(v)
    # Unpack list of activity_time_list_60 (list of lists)
    new_activity_list_60 = []
    for unpack_times in activity_time_list_60:
        new_activity_list_60.append(*unpack_times)
    est_time_60 = tuple(new_activity_list_60)
    total_60_time = 0
    for time_60 in est_time_60:
        sum_times_60 = float(time_60)
        total_60_time += sum_times_60

    # Activity 65
    for k, v in frame_key_time.items():
        if "->65" in k:
            activity_time_list_65.append(v)
    # Unpack list of activity_time_list_65 (list of lists)
    new_activity_list_65 = []
    for unpack_times in activity_time_list_65:
        new_activity_list_65.append(*unpack_times)
    est_time_65 = tuple(new_activity_list_65)
    total_65_time = 0
    for time_65 in est_time_65:
        sum_times_65 = float(time_65)
        total_65_time += sum_times_65

    # Activity 70
    for k, v in frame_key_time.items():
        if "->70" in k:
            activity_time_list_70.append(v)
    # Unpack list of activity_time_list_70 (list of lists)
    new_activity_list_70 = []
    for unpack_times in activity_time_list_70:
        new_activity_list_70.append(*unpack_times)
    est_time_70 = tuple(new_activity_list_70)
    total_70_time = 0
    for time_70 in est_time_70:
        sum_times_70 = float(time_70)
        total_70_time += sum_times_70

    # Refactor time conversion code (now in separate if statements:
    # Function def convert_time(ea_act_time)
    # Unless logic changes, call function for ea time
    # Can string together as if-elif-else and check
    #   value from each function call - return hhmmss

    all_act_times = []
    # convert decimal minutes to hh:mm:ss
    if total_05_time:
        i, d = divmod(total_05_time, 1)
        hh = "00"
        if i < 10:
            i = str(i)
            i = i.split('.')
            mm = f"0{i[0]}"
        else:
            i = str(i)
            i = i.split('.')
            mm = i[0]
        if d:
            d = str(d * 60)
            d = d.split('.')
            ss = d[0]
        else:
            ss = "00"
        hhmmss = f"{hh}:{mm}:{ss}"
        act_time_05 = f"Activity 05 Total Est Time:   {hhmmss}\n"
        hhmmss_05 = hhmmss
        all_act_times.append(hhmmss_05)
    else:
        pass

    if total_10_time:
        i, d = divmod(total_10_time, 1)
        hh = "00"
        if i < 10:
            i = str(i)
            i = i.split('.')
            mm = f"0{i[0]}"
        else:
            i = str(i)
            i = i.split('.')
            mm = i[0]
        if d:
            d = str(d * 60)
            d = d.split('.')
            ss = d[0]
        else:
            ss = "00"
        hhmmss = f"{hh}:{mm}:{ss}"
        act_time_10 = f"Activity 10 Total Est Time:   {hhmmss}\n"
        hhmmss_10 = hhmmss
        all_act_times.append(hhmmss_10)
    else:
        pass

    if total_15_time:
        i, d = divmod(total_15_time, 1)
        hh = "00"
        if i < 10:
            i = str(i)
            i = i.split('.')
            mm = f"0{i[0]}"
        else:
            i = str(i)
            i = i.split('.')
            mm = i[0]
        if d:
            d = str(d * 60)
            d = d.split('.')
            ss = d[0]
        else:
            ss = "00"
        hhmmss = f"{hh}:{mm}:{ss}"
        act_time_15 = f"Activity 15 Total Est Time:   {hhmmss}\n"
        hhmmss_15 = hhmmss
        all_act_times.append(hhmmss_15)
    else:
        pass

    if total_20_time:
        i, d = divmod(total_20_time, 1)
        hh = "00"
        if i < 10:
            i = str(i)
            i = i.split('.')
            mm = f"0{i[0]}"
        else:
            i = str(i)
            i = i.split('.')
            mm = i[0]
        if d:
            d = str(d * 60)
            d = d.split('.')
            ss = d[0]
        else:
            ss = "00"
        hhmmss = f"{hh}:{mm}:{ss}"
        act_time_20 = f"Activity 20 Total Est Time:   {hhmmss}\n"
        hhmmss_20 = hhmmss
        all_act_times.append(hhmmss_20)
    else:
        pass

    if total_25_time:
        i, d = divmod(total_25_time, 1)
        hh = "00"
        if i < 10:
            i = str(i)
            i = i.split('.')
            mm = f"0{i[0]}"
        else:
            i = str(i)
            i = i.split('.')
            mm = i[0]
        if d:
            d = str(d * 60)
            d = d.split('.')
            ss = d[0]
        else:
            ss = "00"
        hhmmss = f"{hh}:{mm}:{ss}"
        act_time_25 = f"Activity 25 Total Est Time:   {hhmmss}\n"
        hhmmss_25 = hhmmss
        all_act_times.append(hhmmss_25)
    else:
        pass

    if total_30_time:
        i, d = divmod(total_30_time, 1)
        hh = "00"
        if i < 10:
            i = str(i)
            i = i.split('.')
            mm = f"0{i[0]}"
        else:
            i = str(i)
            i = i.split('.')
            mm = i[0]
        if d:
            d = str(d * 60)
            d = d.split('.')
            ss = d[0]
        else:
            ss = "00"
        hhmmss = f"{hh}:{mm}:{ss}"
        act_time_30 = f"Activity 30 Total Est Time:   {hhmmss}\n"
        hhmmss_30 = hhmmss
        all_act_times.append(hhmmss_30)
    else:
        pass

    if total_35_time:
        i, d = divmod(total_35_time, 1)
        hh = "00"
        if i < 10:
            i = str(i)
            i = i.split('.')
            mm = f"0{i[0]}"
        else:
            i = str(i)
            i = i.split('.')
            mm = i[0]
        if d:
            d = str(d * 60)
            d = d.split('.')
            ss = d[0]
        else:
            ss = "00"
        hhmmss = f"{hh}:{mm}:{ss}"
        act_time_35 = f"Activity 35 Total Est Time:   {hhmmss}\n"
        hhmmss_35 = hhmmss
        all_act_times.append(hhmmss_35)
    else:
        pass

    if total_40_time:
        i, d = divmod(total_40_time, 1)
        hh = "00"
        if i < 10:
            i = str(i)
            i = i.split('.')
            mm = f"0{i[0]}"
        else:
            i = str(i)
            i = i.split('.')
            mm = i[0]
        if d:
            d = str(d * 60)
            d = d.split('.')
            ss = d[0]
        else:
            ss = "00"
        hhmmss = f"{hh}:{mm}:{ss}"
        act_time_40 = f"Activity 40 Total Est Time:   {hhmmss}\n"
        hhmmss_40 = hhmmss
        all_act_times.append(hhmmss_40)
    else:
        pass
    if total_45_time:
        i, d = divmod(total_45_time, 1)
        hh = "00"
        if i < 10:
            i = str(i)
            i = i.split('.')
            mm = f"0{i[0]}"
        else:
            i = str(i)
            i = i.split('.')
            mm = i[0]
        if d:
            d = str(d * 60)
            d = d.split('.')
            ss = d[0]
        else:
            ss = "00"
        hhmmss = f"{hh}:{mm}:{ss}"
        act_time_45 = f"Activity 45 Total Est Time:   {hhmmss}\n"
        hhmmss_45 = hhmmss
        all_act_times.append(hhmmss_45)
    else:
        pass

    if total_50_time:
        # convert decimal minutes to hh:mm:ss
        i, d = divmod(total_50_time, 1)
        hh = "00"
        if i < 10:
            i = str(i)
            i = i.split('.')
            mm = f"0{i[0]}"
        else:
            i = str(i)
            i = i.split('.')
            mm = i[0]
        if d:
            d = str(d * 60)
            d = d.split('.')
            ss = d[0]
        else:
            ss = "00"
        hhmmss = f"{hh}:{mm}:{ss}"
        # print(f"Activity 50 Total Est Time: {hhmmss}\n")
        act_time_50 = f"Activity 50 Total Est Time:   {hhmmss}\n"
        hhmmss_50 = hhmmss
        all_act_times.append(hhmmss_50)
    else:
        pass

    if total_55_time:
        i, d = divmod(total_55_time, 1)
        hh = "00"
        if i < 10:
            i = str(i)
            i = i.split('.')
            mm = f"0{i[0]}"
        else:
            i = str(i)
            i = i.split('.')
            mm = i[0]
        if d:
            d = str(d * 60)
            d = d.split('.')
            ss = d[0]
        else:
            ss = "00"
        hhmmss = f"{hh}:{mm}:{ss}"
        act_time_55 = f"Activity 55 Total Est Time:   {hhmmss}\n"
        hhmmss_55 = hhmmss
        all_act_times.append(hhmmss_55)
    else:
        pass

    if total_60_time:
        i, d = divmod(total_60_time, 1)
        hh = "00"
        if i < 10:
            i = str(i)
            i = i.split('.')
            mm = f"0{i[0]}"
        else:
            i = str(i)
            i = i.split('.')
            mm = i[0]
        if d:
            d = str(d * 60)
            d = d.split('.')
            ss = d[0]
        else:
            ss = "00"
        hhmmss = f"{hh}:{mm}:{ss}"
        act_time_60 = f"Activity 60 Total Est Time:   {hhmmss}\n"
        hhmmss_60 = hhmmss
        all_act_times.append(hhmmss_60)
    else:
        pass

    if total_65_time:
        i, d = divmod(total_65_time, 1)
        hh = "00"
        if i < 10:
            i = str(i)
            i = i.split('.')
            mm = f"0{i[0]}"
        else:
            i = str(i)
            i = i.split('.')
            mm = i[0]
        if d:
            d = str(d * 60)
            d = d.split('.')
            ss = d[0]
        else:
            ss = "00"
        hhmmss = f"{hh}:{mm}:{ss}"
        act_time_65 = f"Activity 65 Total Est Time:   {hhmmss}\n"
        hhmmss_65 = hhmmss
        all_act_times.append(hhmmss_65)
    else:
        pass

    if total_70_time:
        i, d = divmod(total_70_time, 1)
        hh = "00"
        if i < 10:
            i = str(i)
            i = i.split('.')
            mm = f"0{i[0]}"
        else:
            i = str(i)
            i = i.split('.')
            mm = i[0]
        if d:
            d = str(d * 60)
            d = d.split('.')
            ss = d[0]
        else:
            ss = "00"
        hhmmss = f"{hh}:{mm}:{ss}"
        act_time_70 = f"Activity 70 Total Est Time:   {hhmmss}\n"
        hhmmss_70 = hhmmss
        all_act_times.append(hhmmss_70)
    else:
        pass

    # Write activity times to the extraction sheet
    get_len = len(all_act_times)
    i = 0
    row = 10
    col = 0
    for act_time_el in all_act_times:
        while i < get_len:
            for ext_data in ext_sheet_data:
                if 'fc' in ext_data:
                    worksheet1.write(
                        row, 9, all_act_times[i], ext_sht_content_line)
                    i += 1
                else:
                    pass
                if 'ea' in ext_data:
                    worksheet1.write(
                        row, 9, all_act_times[i], ext_sht_content_line)
                    i += 1
                else:
                    pass
                if 'sw' in ext_data:
                    worksheet1.write(
                        row, 9, all_act_times[i], ext_sht_content_line)
                    i += 1
                else:
                    pass
                if 'uc' in ext_data:
                    worksheet1.write(
                        row, 9, all_act_times[i], ext_sht_content_line)
                    i += 1
                else:
                    pass
                row += 1

    workbook.close()

# #######  Build the directory of folders ########


def directory_out(frame_set, f_name):
    '''Build, format, and write directory.'''

    print(
        f"{slide_break}\nDirectory build, Extraction XLSX, "
        f"PPTX copy: ** SUCCESS **\n{slide_break}"
    )

    for frame in frame_set:
        abs_dir = "c:\\e2020_tool_data\\output"
        # print(frame)
        # m = mbid; u = unit; l = lesson; a = activity; fr = frame
        if len(f_name) == 10:
            m = frame[0:4]
            u = frame[4:7]
            l = frame[7:10]
            a = frame[10:13]
            fr = frame[13:16]

        if len(f_name) == 11:
            m = frame[0:5]
            u = frame[5:8]
            l = frame[8:11]
            a = frame[11:14]
            fr = frame[14:17]

        file_dir_structure = f"{abs_dir}\\{m}\\{m}{u}\\{m}{u}{l}"
        file_dir_structure += f"\\{m}{u}{l}{a}\\{m}{u}{l}{a}{fr}"

        if not os.path.exists(f"{file_dir_structure}"):
            os.makedirs(f"{file_dir_structure}")

        # print(f"{file_dir_structure}\n")


def copy_pptx(nav_dir, src_path_file, dest_path):
    """Copy the PPTX file to the output folder."""
    os.chdir(nav_dir)
    shutil.copy(src_path_file, dest_path)
    app_kill()

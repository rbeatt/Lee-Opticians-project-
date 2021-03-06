#############################################################################
# Generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#  Mar 26, 2021 08:51:19 PM GMT  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { \
    leeopticianslogo_jpg "../Users/ryanb/OneDrive - C2k/A2 2020-2021/Computer Science/A2 Unit 5/Code/LeeOpticianslogo.jpg" \
}
vTcl:create_project_images $image_list   ;# In image.tcl


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(pr,menufgcolor) #000000
set vTcl(pr,menubgcolor) #d9d9d9
set vTcl(pr,menuanalogcolor) #ececec
set vTcl(pr,treehighlight) firebrick
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}



    menu .pop49 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 1 
    vTcl:DefineAlias ".pop49" "Popupmenu1" vTcl:WidgetProc "" 1

proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background #ffffff 
    wm focusmodel $top passive
    wm geometry $top 600x696+396+0
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1370 749
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm deiconify $top
    wm title $top "Staff Form"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    label $top.lab45 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -image leeopticianslogo_jpg -text Label 
    vTcl:DefineAlias "$top.lab45" "Label1" vTcl:WidgetProc "Toplevel1" 1
    frame $top.fra46 \
        -borderwidth 2 -relief groove -background #ffffff -height 395 \
        -width 125 
    vTcl:DefineAlias "$top.fra46" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra46
    button $site_3_0.but67 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Add 
    vTcl:DefineAlias "$site_3_0.but67" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but68 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Search 
    vTcl:DefineAlias "$site_3_0.but68" "Button2" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but69 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Delete 
    vTcl:DefineAlias "$site_3_0.but69" "Button3" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but70 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Update 
    vTcl:DefineAlias "$site_3_0.but70" "Button4" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but71 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Close Form} 
    vTcl:DefineAlias "$site_3_0.but71" "Button5" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.but67 \
        -in $site_3_0 -x 0 -relx 0.24 -y 0 -rely 0.051 -width 67 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but68 \
        -in $site_3_0 -x 0 -relx 0.24 -y 0 -rely 0.177 -width 67 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but69 \
        -in $site_3_0 -x 0 -relx 0.24 -y 0 -rely 0.304 -width 67 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but70 \
        -in $site_3_0 -x 0 -relx 0.24 -y 0 -rely 0.43 -width 67 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but71 \
        -in $site_3_0 -x 0 -relx 0.16 -y 0 -rely 0.886 -width 87 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    entry $top.ent47 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 294 
    vTcl:DefineAlias "$top.ent47" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent48 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 294 
    vTcl:DefineAlias "$top.ent48" "Entry2" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent50 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 294 
    vTcl:DefineAlias "$top.ent50" "Entry3" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent51 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 294 
    vTcl:DefineAlias "$top.ent51" "Entry4" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent52 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 294 
    vTcl:DefineAlias "$top.ent52" "Entry5" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent53 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 294 
    vTcl:DefineAlias "$top.ent53" "Entry6" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent54 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 294 
    vTcl:DefineAlias "$top.ent54" "Entry7" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent55 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 294 
    vTcl:DefineAlias "$top.ent55" "Entry8" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent56 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 294 
    vTcl:DefineAlias "$top.ent56" "Entry9" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab57 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text StaffID 
    vTcl:DefineAlias "$top.lab57" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab58 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text BranchID 
    vTcl:DefineAlias "$top.lab58" "Label3" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab59 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Name 
    vTcl:DefineAlias "$top.lab59" "Label4" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab60 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Surname 
    vTcl:DefineAlias "$top.lab60" "Label5" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab61 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Position 
    vTcl:DefineAlias "$top.lab61" "Label6" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab62 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Email 
    vTcl:DefineAlias "$top.lab62" "Label7" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab63 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Telephone 
    vTcl:DefineAlias "$top.lab63" "Label8" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab65 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Password 
    vTcl:DefineAlias "$top.lab65" "Label9" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab66 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text AccessLevel 
    vTcl:DefineAlias "$top.lab66" "Label10" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab45 \
        -in $top -x 0 -relx 0.35 -y 0 -rely 0.129 -width 0 -relwidth 0.29 \
        -height 0 -relheight 0.073 -anchor nw -bordermode ignore 
    place $top.fra46 \
        -in $top -x 0 -relx 0.7 -y 0 -rely 0.273 -width 0 -relwidth 0.208 \
        -height 0 -relheight 0.568 -anchor nw -bordermode ignore 
    place $top.ent47 \
        -in $top -x 0 -relx 0.167 -y 0 -rely 0.302 -width 294 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent48 \
        -in $top -x 0 -relx 0.167 -y 0 -rely 0.359 -width 294 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent50 \
        -in $top -x 0 -relx 0.167 -y 0 -rely 0.417 -width 294 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent51 \
        -in $top -x 0 -relx 0.167 -y 0 -rely 0.474 -width 294 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent52 \
        -in $top -x 0 -relx 0.167 -y 0 -rely 0.532 -width 294 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent53 \
        -in $top -x 0 -relx 0.167 -y 0 -rely 0.589 -width 294 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent54 \
        -in $top -x 0 -relx 0.167 -y 0 -rely 0.647 -width 294 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent55 \
        -in $top -x 0 -relx 0.167 -y 0 -rely 0.704 -width 294 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent56 \
        -in $top -x 0 -relx 0.167 -y 0 -rely 0.761 -width 294 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab57 \
        -in $top -x 0 -relx 0.067 -y 0 -rely 0.302 -width 0 -relwidth 0.09 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab58 \
        -in $top -x 0 -relx 0.05 -y 0 -rely 0.359 -width 0 -relwidth 0.107 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab59 \
        -in $top -x 0 -relx 0.067 -y 0 -rely 0.417 -width 0 -relwidth 0.09 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab60 \
        -in $top -x 0 -relx 0.05 -y 0 -rely 0.474 -width 0 -relwidth 0.107 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab61 \
        -in $top -x 0 -relx 0.05 -y 0 -rely 0.532 -width 0 -relwidth 0.107 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab62 \
        -in $top -x 0 -relx 0.067 -y 0 -rely 0.589 -width 0 -relwidth 0.09 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab63 \
        -in $top -x 0 -relx 0.033 -y 0 -rely 0.647 -width 0 -relwidth 0.123 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab65 \
        -in $top -x 0 -relx 0.05 -y 0 -rely 0.704 -width 0 -relwidth 0.107 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab66 \
        -in $top -x 0 -relx 0.033 -y 0 -rely 0.761 -width 0 -relwidth 0.123 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}


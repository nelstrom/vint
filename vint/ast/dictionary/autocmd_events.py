from enum import Enum, unique


@unique
class AutocmdEvents(Enum):
    BUF_ADD = 'BufAdd'
    BUF_CREATE = 'BufCreate'
    BUF_DELETE = 'BufDelete'
    BUF_ENTER = 'BufEnter'
    BUF_FILE_POST = 'BufFilePost'
    BUF_FILE_PRE = 'BufFilePre'
    BUF_HIDDEN = 'BufHidden'
    BUF_LEAVE = 'BufLeave'
    BUF_NEW = 'BufNew'
    BUF_NEW_FILE = 'BufNewFile'
    BUF_READ = 'BufRead'
    BUF_READ_CMD = 'BufReadCmd'
    BUF_READ_POST = 'BufReadPost'
    BUF_READ_PRE = 'BufReadPre'
    BUF_UNLOAD = 'BufUnload'
    BUF_WIN_ENTER = 'BufWinEnter'
    BUF_WIN_LEAVE = 'BufWinLeave'
    BUF_WIPEOUT = 'BufWipeout'
    BUF_WRITE = 'BufWrite'
    BUF_WRITE_CMD = 'BufWriteCmd'
    BUF_WRITE_POST = 'BufWritePost'
    BUF_WRITE_PRE = 'BufWritePre'
    CMD_UNDEFINED = 'CmdUndefined'
    CMDWIN_ENTER = 'CmdwinEnter'
    CMDWIN_LEAVE = 'CmdwinLeave'
    COLOR_SCHEME = 'ColorScheme'
    COMPLETE_DONE = 'CompleteDone'
    CURSOR_HOLD = 'CursorHold'
    CURSOR_HOLD_I = 'CursorHoldI'
    CURSOR_MOVED = 'CursorMoved'
    CURSOR_MOVED_I = 'CursorMovedI'
    ENCODING_CHANGED = 'EncodingChanged'
    FILE_APPEND_CMD = 'FileAppendCmd'
    FILE_APPEND_POST = 'FileAppendPost'
    FILE_APPEND_PRE = 'FileAppendPre'
    FILE_CHANGED_RO = 'FileChangedRO'
    FILE_CHANGED_SHELL = 'FileChangedShell'
    FILE_CHANGED_SHELL_POST = 'FileChangedShellPost'
    FILE_READ_CMD = 'FileReadCmd'
    FILE_READ_POST = 'FileReadPost'
    FILE_READ_PRE = 'FileReadPre'
    FILE_TYPE = 'FileType'
    FILE_WRITE_CMD = 'FileWriteCmd'
    FILE_WRITE_POST = 'FileWritePost'
    FILE_WRITE_PRE = 'FileWritePre'
    FILTER_READ_POST = 'FilterReadPost'
    FILTER_READ_PRE = 'FilterReadPre'
    FILTER_WRITE_POST = 'FilterWritePost'
    FILTER_WRITE_PRE = 'FilterWritePre'
    FOCUS_GAINED = 'FocusGained'
    FOCUS_LOST = 'FocusLost'
    FUNC_UNDEFINED = 'FuncUndefined'
    GUI_ENTER = 'GUIEnter'
    GUI_FAILED = 'GUIFailed'
    INSERT_CHANGE = 'InsertChange'
    INSERT_CHAR_PRE = 'InsertCharPre'
    INSERT_ENTER = 'InsertEnter'
    INSERT_LEAVE = 'InsertLeave'
    MENU_POPUP = 'MenuPopup'
    QUICK_FIX_CMD_POST = 'QuickFixCmdPost'
    QUICK_FIX_CMD_PRE = 'QuickFixCmdPre'
    QUIT_PRE = 'QuitPre'
    REMOTE_REPLY = 'RemoteReply'
    SESSION_LOAD_POST = 'SessionLoadPost'
    SHELL_CMD_POST = 'ShellCmdPost'
    SHELL_FILTER_POST = 'ShellFilterPost'
    SOURCE_CMD = 'SourceCmd'
    SOURCE_PRE = 'SourcePre'
    SPELL_FILE_MISSING = 'SpellFileMissing'
    STDIN_READ_POST = 'StdinReadPost'
    STDIN_READ_PRE = 'StdinReadPre'
    SWAP_EXISTS = 'SwapExists'
    SYNTAX = 'Syntax'
    TAB_ENTER = 'TabEnter'
    TAB_LEAVE = 'TabLeave'
    TERM_CHANGED = 'TermChanged'
    TERM_RESPONSE = 'TermResponse'
    TEXT_CHANGED = 'TextChanged'
    TEXT_CHANGED_I = 'TextChangedI'
    USER = 'User'
    VIM_ENTER = 'VimEnter'
    VIM_LEAVE = 'VimLeave'
    VIM_LEAVE_PRE = 'VimLeavePre'
    VIM_RESIZED = 'VimResized'
    WIN_ENTER = 'WinEnter'
    WIN_LEAVE = 'WinLeave'
    ANY = '*'


_autocmd_existence_map = {event.value.lower(): True for event in AutocmdEvents}


def is_autocmd_event(event_name):
    """ Whether the specified string is an autocmd event.
    """
    return _autocmd_existence_map.get(event_name.lower(), False)

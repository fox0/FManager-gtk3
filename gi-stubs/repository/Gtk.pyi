class AboutDialog: ...
class AccelGroup: ...
class AccelLabel: ...
class AccelMap: ...
class Accessible: ...
class Action: ...
class ActionBar: ...
class ActionGroup: ...
class Actionable: ...
class Activatable: ...
class Adjustment: ...
class Alignment: ...
class AppChooser: ...
class AppChooserButton: ...
class AppChooserDialog: ...
class AppChooserWidget: ...
class Application: ...
class ApplicationWindow: ...
class Arrow: ...
class ArrowAccessible: ...
class AspectFrame: ...
class Assistant: ...
class Bin: ...
class BooleanCellAccessible: ...
class Box: ...
class Buildable: ...
class Builder: ...

# fox
class Button:
    def __init__(self, label: str = None): ...
    def connect(self, signal: str, callback: callable): ...

class ButtonAccessible: ...
class ButtonBox: ...
class Calendar: ...
class CellAccessible: ...
class CellAccessibleParent: ...
class CellArea: ...
class CellAreaBox: ...
class CellAreaContext: ...
class CellEditable: ...
class CellLayout: ...
class CellRenderer: ...
class CellRendererAccel: ...
class CellRendererCombo: ...
class CellRendererPixbuf: ...
class CellRendererProgress: ...
class CellRendererSpin: ...
class CellRendererSpinner: ...
class CellRendererText: ...
class CellRendererToggle: ...
class CellView: ...
class CheckButton: ...
class CheckMenuItem: ...
class CheckMenuItemAccessible: ...
class Clipboard: ...
class ColorButton: ...
class ColorChooser: ...
class ColorChooserDialog: ...
class ColorChooserWidget: ...
class ColorSelection: ...
class ColorSelectionDialog: ...
class ComboBox: ...
class ComboBoxAccessible: ...
class ComboBoxText: ...
class Container: ...
class ContainerAccessible: ...
class ContainerCellAccessible: ...
class CssProvider: ...
class Dialog: ...
class DrawingArea: ...
class Editable: ...
class Entry: ...
class EntryAccessible: ...
class EntryBuffer: ...
class EntryCompletion: ...
class EntryIconAccessible: ...
class EventBox: ...
class EventController: ...
class EventControllerKey: ...
class EventControllerMotion: ...
class EventControllerScroll: ...
class Expander: ...
class ExpanderAccessible: ...
class FileChooser: ...
class FileChooserButton: ...
class FileChooserDialog: ...
class FileChooserNative: ...
class FileChooserWidget: ...
class FileFilter: ...
class Fixed: ...
class FlowBox: ...
class FlowBoxAccessible: ...
class FlowBoxChild: ...
class FlowBoxChildAccessible: ...
class FontButton: ...
class FontChooser: ...
class FontChooserDialog: ...
class FontChooserWidget: ...
class FontSelection: ...
class FontSelectionDialog: ...
class Frame: ...
class FrameAccessible: ...
class GLArea: ...
class Gesture: ...
class GestureDrag: ...
class GestureLongPress: ...
class GestureMultiPress: ...
class GesturePan: ...
class GestureRotate: ...
class GestureSingle: ...
class GestureStylus: ...
class GestureSwipe: ...
class GestureZoom: ...
class Grid: ...
class HBox: ...
class HButtonBox: ...
class HPaned: ...
class HSV: ...
class HScale: ...
class HScrollbar: ...
class HSeparator: ...
class HandleBox: ...
class HeaderBar: ...
class IMContext: ...
class IMContextSimple: ...
class IMMulticontext: ...
class IconFactory: ...
class IconInfo: ...
class IconTheme: ...
class IconView: ...
class IconViewAccessible: ...
class Image: ...
class ImageAccessible: ...
class ImageCellAccessible: ...
class ImageMenuItem: ...
class InfoBar: ...
class Invisible: ...
class Label: ...
class LabelAccessible: ...
class Layout: ...
class LevelBar: ...
class LevelBarAccessible: ...
class LinkButton: ...
class LinkButtonAccessible: ...
class ListBox: ...
class ListBoxAccessible: ...
class ListBoxRow: ...
class ListBoxRowAccessible: ...
class ListStore: ...
class LockButton: ...
class LockButtonAccessible: ...
class Menu: ...
class MenuAccessible: ...
class MenuBar: ...
class MenuButton: ...
class MenuButtonAccessible: ...
class MenuItem: ...
class MenuItemAccessible: ...
class MenuShell: ...
class MenuShellAccessible: ...
class MenuToolButton: ...
class MessageDialog: ...
class Misc: ...
class ModelButton: ...
class MountOperation: ...
class NativeDialog: ...
class Notebook: ...
class NotebookAccessible: ...
class NotebookPageAccessible: ...
class NumerableIcon: ...
class OffscreenWindow: ...
class Orientable: ...
class Overlay: ...
class PadController: ...
class PageSetup: ...
class Paned: ...
class PanedAccessible: ...
class PlacesSidebar: ...
class Plug: ...
class Popover: ...
class PopoverAccessible: ...
class PopoverMenu: ...
class PrintContext: ...
class PrintOperation: ...
class PrintOperationPreview: ...
class PrintSettings: ...
class ProgressBar: ...
class ProgressBarAccessible: ...
class RadioAction: ...
class RadioButton: ...
class RadioButtonAccessible: ...
class RadioMenuItem: ...
class RadioMenuItemAccessible: ...
class RadioToolButton: ...
class Range: ...
class RangeAccessible: ...
class RcStyle: ...
class RecentAction: ...
class RecentChooser: ...
class RecentChooserDialog: ...
class RecentChooserMenu: ...
class RecentChooserWidget: ...
class RecentFilter: ...
class RecentManager: ...
class RendererCellAccessible: ...
class Revealer: ...
class Scale: ...
class ScaleAccessible: ...
class ScaleButton: ...
class ScaleButtonAccessible: ...
class Scrollable: ...
class Scrollbar: ...
class ScrolledWindow: ...
class ScrolledWindowAccessible: ...
class SearchBar: ...
class SearchEntry: ...
class Separator: ...
class SeparatorMenuItem: ...
class SeparatorToolItem: ...
class Settings: ...
class ShortcutLabel: ...
class ShortcutsGroup: ...
class ShortcutsSection: ...
class ShortcutsShortcut: ...
class ShortcutsWindow: ...
class SizeGroup: ...
class Socket: ...
class SpinButton: ...
class SpinButtonAccessible: ...
class Spinner: ...
class SpinnerAccessible: ...
class Stack: ...
class StackAccessible: ...
class StackSidebar: ...
class StackSwitcher: ...
class StatusIcon: ...
class Statusbar: ...
class StatusbarAccessible: ...
class Style: ...
class StyleContext: ...
class StyleProperties: ...
class StyleProvider: ...
class Switch: ...
class SwitchAccessible: ...

# fox
class Table:
    def __init__(self, n_rows: int = None, n_columns: int = None, homogeneous: bool = True): ...
    def attach(self, child, left_attach: int, right_attach: int, top_attach: int, bottom_attach: int): ...

class TearoffMenuItem: ...
class TextBuffer: ...
class TextCellAccessible: ...
class TextChildAnchor: ...
class TextMark: ...
class TextTag: ...
class TextTagTable: ...
class TextView: ...
class TextViewAccessible: ...
class ThemingEngine: ...
class ToggleAction: ...
class ToggleButton: ...
class ToggleButtonAccessible: ...
class ToggleToolButton: ...
class ToolButton: ...
class ToolItem: ...
class ToolItemGroup: ...
class ToolPalette: ...
class ToolShell: ...
class Toolbar: ...
class Tooltip: ...
class ToplevelAccessible: ...
class TreeDragDest: ...
class TreeDragSource: ...
class TreeModel: ...
class TreeModelFilter: ...
class TreeModelSort: ...
class TreeSelection: ...
class TreeSortable: ...
class TreeStore: ...
class TreeView: ...
class TreeViewAccessible: ...
class TreeViewColumn: ...
class UIManager: ...
class VBox: ...
class VButtonBox: ...
class VPaned: ...
class VScale: ...
class VScrollbar: ...
class VSeparator: ...
class Viewport: ...
class VolumeButton: ...
class Widget: ...
class WidgetAccessible: ...

# fox
class Window:
    def __init__(self, title: str = None): ...
    def add(self, widget): ...
    def show_all(self): ...
    def connect(self, signal: str, callback: callable): ...

class WindowAccessible: ...
class WindowGroup: ...
class AccelFlags: ...
class ApplicationInhibitFlags: ...
class AttachOptions: ...
class CalendarDisplayOptions: ...
class CellRendererState: ...
class DebugFlag: ...
class DestDefaults: ...
class DialogFlags: ...
class EventControllerScrollFlags: ...
class FileFilterFlags: ...
class FontChooserLevel: ...
class IconLookupFlags: ...
class InputHints: ...
class JunctionSides: ...
class PlacesOpenFlags: ...
class RcFlags: ...
class RecentFilterFlags: ...
class RegionFlags: ...
class StateFlags: ...
class StyleContextPrintFlags: ...
class TargetFlags: ...
class TextSearchFlags: ...
class ToolPaletteDragTargets: ...
class TreeModelFlags: ...
class UIManagerItemType: ...
class Align: ...
class ArrowPlacement: ...
class ArrowType: ...
class AssistantPageType: ...
class BaselinePosition: ...
class BorderStyle: ...
class BuilderError: ...
class ButtonBoxStyle: ...
class ButtonRole: ...
class ButtonsType: ...
class CellRendererAccelMode: ...
class CellRendererMode: ...
class CornerType: ...
class CssProviderError: ...
class CssSectionType: ...
class DeleteType: ...
class DirectionType: ...
class DragResult: ...
class EntryIconPosition: ...
class EventSequenceState: ...
class ExpanderStyle: ...
class FileChooserAction: ...
class FileChooserConfirmation: ...
class FileChooserError: ...
class IMPreeditStyle: ...
class IMStatusStyle: ...
class IconSize: ...
class IconThemeError: ...
class IconViewDropPosition: ...
class ImageType: ...
class InputPurpose: ...
class Justification: ...
class LevelBarMode: ...
class License: ...
class MenuDirectionType: ...
class MessageType: ...
class MovementStep: ...
class NotebookTab: ...
class NumberUpLayout: ...
class Orientation: ...
class PackDirection: ...
class PackType: ...
class PadActionType: ...
class PageOrientation: ...
class PageSet: ...
class PanDirection: ...
class PathPriorityType: ...
class PathType: ...
class PolicyType: ...
class PopoverConstraint: ...
class PositionType: ...
class PrintDuplex: ...
class PrintError: ...
class PrintOperationAction: ...
class PrintOperationResult: ...
class PrintPages: ...
class PrintQuality: ...
class PrintStatus: ...
class PropagationPhase: ...
class RcTokenType: ...
class RecentChooserError: ...
class RecentManagerError: ...
class RecentSortType: ...
class ReliefStyle: ...
class ResizeMode: ...
class ResponseType: ...
class RevealerTransitionType: ...
class ScrollStep: ...
class ScrollType: ...
class ScrollablePolicy: ...
class SelectionMode: ...
class SensitivityType: ...
class ShadowType: ...
class ShortcutType: ...
class SizeGroupMode: ...
class SizeRequestMode: ...
class SortType: ...
class SpinButtonUpdatePolicy: ...
class SpinType: ...
class StackTransitionType: ...
class StateType: ...
class TextBufferTargetInfo: ...
class TextDirection: ...
class TextExtendSelection: ...
class TextViewLayer: ...
class TextWindowType: ...
class ToolbarSpaceStyle: ...
class ToolbarStyle: ...
class TreeViewColumnSizing: ...
class TreeViewDropPosition: ...
class TreeViewGridLines: ...
class Unit: ...
class WidgetHelpType: ...
class WindowPosition: ...
class WindowType: ...
class WrapMode: ...
class AccelGroupEntry: ...
class AccelKey: ...
class ActionEntry: ...
class BindingArg: ...
class BindingEntry: ...
class BindingSet: ...
class BindingSignal: ...
class Border: ...
class CssSection: ...
class FileFilterInfo: ...
class FixedChild: ...
class Gradient: ...
class IMContextInfo: ...
class IconSet: ...
class IconSource: ...
class PadActionEntry: ...
class PageRange: ...
class PaperSize: ...
class RadioActionEntry: ...
class RcProperty: ...
class RecentData: ...
class RecentFilterInfo: ...
class RecentInfo: ...
class RequestedSize: ...
class Requisition: ...
class SelectionData: ...
class SettingsValue: ...
class StockItem: ...
class SymbolicColor: ...
class TableChild: ...
class TableRowCol: ...
class TargetEntry: ...
class TargetList: ...
class TargetPair: ...
class TextAppearance: ...
class TextAttributes: ...
class TextIter: ...
class ToggleActionEntry: ...
class TreeIter: ...
class TreePath: ...
class TreeRowReference: ...
class WidgetPath: ...

def accel_groups_activate(*args, **kwargs): ...
def accel_groups_from_object(*args, **kwargs): ...
def accelerator_get_default_mod_mask(*args, **kwargs): ...
def accelerator_get_label(*args, **kwargs): ...
def accelerator_get_label_with_keycode(*args, **kwargs): ...
def accelerator_name(*args, **kwargs): ...
def accelerator_name_with_keycode(*args, **kwargs): ...
def accelerator_parse(*args, **kwargs): ...
def accelerator_parse_with_keycode(*args, **kwargs): ...
def accelerator_set_default_mod_mask(*args, **kwargs): ...
def accelerator_valid(*args, **kwargs): ...
def alternative_dialog_button_order(*args, **kwargs): ...
def binding_entry_add_signal_from_string(*args, **kwargs): ...
def binding_entry_add_signall(*args, **kwargs): ...
def binding_entry_remove(*args, **kwargs): ...
def binding_entry_skip(*args, **kwargs): ...
def binding_set_find(*args, **kwargs): ...
def bindings_activate(*args, **kwargs): ...
def bindings_activate_event(*args, **kwargs): ...
def builder_error_quark(*args, **kwargs): ...
def cairo_should_draw_window(*args, **kwargs): ...
def cairo_transform_to_window(*args, **kwargs): ...
def check_version(*args, **kwargs): ...
def css_provider_error_quark(*args, **kwargs): ...
def device_grab_add(*args, **kwargs): ...
def device_grab_remove(*args, **kwargs): ...
def disable_setlocale(*args, **kwargs): ...
def distribute_natural_allocation(*args, **kwargs): ...
def drag_cancel(*args, **kwargs): ...
def drag_finish(*args, **kwargs): ...
def drag_get_source_widget(*args, **kwargs): ...
def drag_set_icon_default(*args, **kwargs): ...
def drag_set_icon_gicon(*args, **kwargs): ...
def drag_set_icon_name(*args, **kwargs): ...
def drag_set_icon_pixbuf(*args, **kwargs): ...
def drag_set_icon_stock(*args, **kwargs): ...
def drag_set_icon_surface(*args, **kwargs): ...
def drag_set_icon_widget(*args, **kwargs): ...
def draw_insertion_cursor(*args, **kwargs): ...
def events_pending(*args, **kwargs): ...
def false(*args, **kwargs): ...
def file_chooser_error_quark(*args, **kwargs): ...
def get_binary_age(*args, **kwargs): ...
def get_current_event(*args, **kwargs): ...
def get_current_event_device(*args, **kwargs): ...
def get_current_event_state(*args, **kwargs): ...
def get_current_event_time(*args, **kwargs): ...
def get_debug_flags(*args, **kwargs): ...
def get_default_language(*args, **kwargs): ...
def get_event_widget(*args, **kwargs): ...
def get_interface_age(*args, **kwargs): ...
def get_locale_direction(*args, **kwargs): ...
def get_major_version(*args, **kwargs): ...
def get_micro_version(*args, **kwargs): ...
def get_minor_version(*args, **kwargs): ...
def get_option_group(*args, **kwargs): ...
def grab_get_current(*args, **kwargs): ...
def icon_size_from_name(*args, **kwargs): ...
def icon_size_get_name(*args, **kwargs): ...
def icon_size_lookup(*args, **kwargs): ...
def icon_size_lookup_for_settings(*args, **kwargs): ...
def icon_size_register(*args, **kwargs): ...
def icon_size_register_alias(*args, **kwargs): ...
def icon_theme_error_quark(*args, **kwargs): ...
def init(*args, **kwargs): ...
def init_check(*args, **kwargs): ...
def init_with_args(*args, **kwargs): ...
def key_snooper_remove(*args, **kwargs): ...
def main(*args, **kwargs): ...
def main_do_event(*args, **kwargs): ...
def main_iteration(*args, **kwargs): ...
def main_iteration_do(*args, **kwargs): ...
def main_level(*args, **kwargs): ...
def main_quit(*args, **kwargs): ...
def paint_arrow(*args, **kwargs): ...
def paint_box(*args, **kwargs): ...
def paint_box_gap(*args, **kwargs): ...
def paint_check(*args, **kwargs): ...
def paint_diamond(*args, **kwargs): ...
def paint_expander(*args, **kwargs): ...
def paint_extension(*args, **kwargs): ...
def paint_flat_box(*args, **kwargs): ...
def paint_focus(*args, **kwargs): ...
def paint_handle(*args, **kwargs): ...
def paint_hline(*args, **kwargs): ...
def paint_layout(*args, **kwargs): ...
def paint_option(*args, **kwargs): ...
def paint_resize_grip(*args, **kwargs): ...
def paint_shadow(*args, **kwargs): ...
def paint_shadow_gap(*args, **kwargs): ...
def paint_slider(*args, **kwargs): ...
def paint_spinner(*args, **kwargs): ...
def paint_tab(*args, **kwargs): ...
def paint_vline(*args, **kwargs): ...
def paper_size_get_default(*args, **kwargs): ...
def paper_size_get_paper_sizes(*args, **kwargs): ...
def parse_args(*args, **kwargs): ...
def print_error_quark(*args, **kwargs): ...
def print_run_page_setup_dialog(*args, **kwargs): ...
def print_run_page_setup_dialog_async(*args, **kwargs): ...
def propagate_event(*args, **kwargs): ...
def rc_add_default_file(*args, **kwargs): ...
def rc_find_module_in_path(*args, **kwargs): ...
def rc_find_pixmap_in_path(*args, **kwargs): ...
def rc_get_default_files(*args, **kwargs): ...
def rc_get_im_module_file(*args, **kwargs): ...
def rc_get_im_module_path(*args, **kwargs): ...
def rc_get_module_dir(*args, **kwargs): ...
def rc_get_style(*args, **kwargs): ...
def rc_get_style_by_paths(*args, **kwargs): ...
def rc_get_theme_dir(*args, **kwargs): ...
def rc_parse(*args, **kwargs): ...
def rc_parse_color(*args, **kwargs): ...
def rc_parse_color_full(*args, **kwargs): ...
def rc_parse_priority(*args, **kwargs): ...
def rc_parse_state(*args, **kwargs): ...
def rc_parse_string(*args, **kwargs): ...
def rc_property_parse_border(*args, **kwargs): ...
def rc_property_parse_color(*args, **kwargs): ...
def rc_property_parse_enum(*args, **kwargs): ...
def rc_property_parse_flags(*args, **kwargs): ...
def rc_property_parse_requisition(*args, **kwargs): ...
def rc_reparse_all(*args, **kwargs): ...
def rc_reparse_all_for_settings(*args, **kwargs): ...
def rc_reset_styles(*args, **kwargs): ...
def rc_set_default_files(*args, **kwargs): ...
def recent_chooser_error_quark(*args, **kwargs): ...
def recent_manager_error_quark(*args, **kwargs): ...
def render_activity(*args, **kwargs): ...
def render_arrow(*args, **kwargs): ...
def render_background(*args, **kwargs): ...
def render_background_get_clip(*args, **kwargs): ...
def render_check(*args, **kwargs): ...
def render_expander(*args, **kwargs): ...
def render_extension(*args, **kwargs): ...
def render_focus(*args, **kwargs): ...
def render_frame(*args, **kwargs): ...
def render_frame_gap(*args, **kwargs): ...
def render_handle(*args, **kwargs): ...
def render_icon(*args, **kwargs): ...
def render_icon_pixbuf(*args, **kwargs): ...
def render_icon_surface(*args, **kwargs): ...
def render_insertion_cursor(*args, **kwargs): ...
def render_layout(*args, **kwargs): ...
def render_line(*args, **kwargs): ...
def render_option(*args, **kwargs): ...
def render_slider(*args, **kwargs): ...
def rgb_to_hsv(*args, **kwargs): ...
def selection_add_target(*args, **kwargs): ...
def selection_add_targets(*args, **kwargs): ...
def selection_clear_targets(*args, **kwargs): ...
def selection_convert(*args, **kwargs): ...
def selection_owner_set(*args, **kwargs): ...
def selection_owner_set_for_display(*args, **kwargs): ...
def selection_remove_all(*args, **kwargs): ...
def set_debug_flags(*args, **kwargs): ...
def show_uri(*args, **kwargs): ...
def show_uri_on_window(*args, **kwargs): ...
def stock_add(*args, **kwargs): ...
def stock_add_static(*args, **kwargs): ...
def stock_list_ids(*args, **kwargs): ...
def stock_lookup(*args, **kwargs): ...
def stock_set_translate_func(*args, **kwargs): ...
def target_table_free(*args, **kwargs): ...
def target_table_new_from_list(*args, **kwargs): ...
def targets_include_image(*args, **kwargs): ...
def targets_include_rich_text(*args, **kwargs): ...
def targets_include_text(*args, **kwargs): ...
def targets_include_uri(*args, **kwargs): ...
def test_create_simple_window(*args, **kwargs): ...
def test_find_label(*args, **kwargs): ...
def test_find_sibling(*args, **kwargs): ...
def test_find_widget(*args, **kwargs): ...
def test_list_all_types(*args, **kwargs): ...
def test_register_all_types(*args, **kwargs): ...
def test_slider_get_value(*args, **kwargs): ...
def test_slider_set_perc(*args, **kwargs): ...
def test_spin_button_click(*args, **kwargs): ...
def test_text_get(*args, **kwargs): ...
def test_text_set(*args, **kwargs): ...
def test_widget_click(*args, **kwargs): ...
def test_widget_send_key(*args, **kwargs): ...
def test_widget_wait_for_draw(*args, **kwargs): ...
def tree_get_row_drag_data(*args, **kwargs): ...
def tree_row_reference_deleted(*args, **kwargs): ...
def tree_row_reference_inserted(*args, **kwargs): ...
def tree_set_row_drag_data(*args, **kwargs): ...
def true(*args, **kwargs): ...

BINARY_AGE = ...
INPUT_ERROR = ...
INTERFACE_AGE = ...
LEVEL_BAR_OFFSET_FULL = ...
LEVEL_BAR_OFFSET_HIGH = ...
LEVEL_BAR_OFFSET_LOW = ...
MAJOR_VERSION = ...
MAX_COMPOSE_LEN = ...
MICRO_VERSION = ...
MINOR_VERSION = ...
PAPER_NAME_A3 = ...
PAPER_NAME_A4 = ...
PAPER_NAME_A5 = ...
PAPER_NAME_B5 = ...
PAPER_NAME_EXECUTIVE = ...
PAPER_NAME_LEGAL = ...
PAPER_NAME_LETTER = ...
PATH_PRIO_MASK = ...
PRINT_SETTINGS_COLLATE = ...
PRINT_SETTINGS_DEFAULT_SOURCE = ...
PRINT_SETTINGS_DITHER = ...
PRINT_SETTINGS_DUPLEX = ...
PRINT_SETTINGS_FINISHINGS = ...
PRINT_SETTINGS_MEDIA_TYPE = ...
PRINT_SETTINGS_NUMBER_UP = ...
PRINT_SETTINGS_NUMBER_UP_LAYOUT = ...
PRINT_SETTINGS_N_COPIES = ...
PRINT_SETTINGS_ORIENTATION = ...
PRINT_SETTINGS_OUTPUT_BASENAME = ...
PRINT_SETTINGS_OUTPUT_BIN = ...
PRINT_SETTINGS_OUTPUT_DIR = ...
PRINT_SETTINGS_OUTPUT_FILE_FORMAT = ...
PRINT_SETTINGS_OUTPUT_URI = ...
PRINT_SETTINGS_PAGE_RANGES = ...
PRINT_SETTINGS_PAGE_SET = ...
PRINT_SETTINGS_PAPER_FORMAT = ...
PRINT_SETTINGS_PAPER_HEIGHT = ...
PRINT_SETTINGS_PAPER_WIDTH = ...
PRINT_SETTINGS_PRINTER = ...
PRINT_SETTINGS_PRINTER_LPI = ...
PRINT_SETTINGS_PRINT_PAGES = ...
PRINT_SETTINGS_QUALITY = ...
PRINT_SETTINGS_RESOLUTION = ...
PRINT_SETTINGS_RESOLUTION_X = ...
PRINT_SETTINGS_RESOLUTION_Y = ...
PRINT_SETTINGS_REVERSE = ...
PRINT_SETTINGS_SCALE = ...
PRINT_SETTINGS_USE_COLOR = ...
PRINT_SETTINGS_WIN32_DRIVER_EXTRA = ...
PRINT_SETTINGS_WIN32_DRIVER_VERSION = ...
PRIORITY_RESIZE = ...
STOCK_ABOUT = ...
STOCK_ADD = ...
STOCK_APPLY = ...
STOCK_BOLD = ...
STOCK_CANCEL = ...
STOCK_CAPS_LOCK_WARNING = ...
STOCK_CDROM = ...
STOCK_CLEAR = ...
STOCK_CLOSE = ...
STOCK_COLOR_PICKER = ...
STOCK_CONNECT = ...
STOCK_CONVERT = ...
STOCK_COPY = ...
STOCK_CUT = ...
STOCK_DELETE = ...
STOCK_DIALOG_AUTHENTICATION = ...
STOCK_DIALOG_ERROR = ...
STOCK_DIALOG_INFO = ...
STOCK_DIALOG_QUESTION = ...
STOCK_DIALOG_WARNING = ...
STOCK_DIRECTORY = ...
STOCK_DISCARD = ...
STOCK_DISCONNECT = ...
STOCK_DND = ...
STOCK_DND_MULTIPLE = ...
STOCK_EDIT = ...
STOCK_EXECUTE = ...
STOCK_FILE = ...
STOCK_FIND = ...
STOCK_FIND_AND_REPLACE = ...
STOCK_FLOPPY = ...
STOCK_FULLSCREEN = ...
STOCK_GOTO_BOTTOM = ...
STOCK_GOTO_FIRST = ...
STOCK_GOTO_LAST = ...
STOCK_GOTO_TOP = ...
STOCK_GO_BACK = ...
STOCK_GO_DOWN = ...
STOCK_GO_FORWARD = ...
STOCK_GO_UP = ...
STOCK_HARDDISK = ...
STOCK_HELP = ...
STOCK_HOME = ...
STOCK_INDENT = ...
STOCK_INDEX = ...
STOCK_INFO = ...
STOCK_ITALIC = ...
STOCK_JUMP_TO = ...
STOCK_JUSTIFY_CENTER = ...
STOCK_JUSTIFY_FILL = ...
STOCK_JUSTIFY_LEFT = ...
STOCK_JUSTIFY_RIGHT = ...
STOCK_LEAVE_FULLSCREEN = ...
STOCK_MEDIA_FORWARD = ...
STOCK_MEDIA_NEXT = ...
STOCK_MEDIA_PAUSE = ...
STOCK_MEDIA_PLAY = ...
STOCK_MEDIA_PREVIOUS = ...
STOCK_MEDIA_RECORD = ...
STOCK_MEDIA_REWIND = ...
STOCK_MEDIA_STOP = ...
STOCK_MISSING_IMAGE = ...
STOCK_NETWORK = ...
STOCK_NEW = ...
STOCK_NO = ...
STOCK_OK = ...
STOCK_OPEN = ...
STOCK_ORIENTATION_LANDSCAPE = ...
STOCK_ORIENTATION_PORTRAIT = ...
STOCK_ORIENTATION_REVERSE_LANDSCAPE = ...
STOCK_ORIENTATION_REVERSE_PORTRAIT = ...
STOCK_PAGE_SETUP = ...
STOCK_PASTE = ...
STOCK_PREFERENCES = ...
STOCK_PRINT = ...
STOCK_PRINT_ERROR = ...
STOCK_PRINT_PAUSED = ...
STOCK_PRINT_PREVIEW = ...
STOCK_PRINT_REPORT = ...
STOCK_PRINT_WARNING = ...
STOCK_PROPERTIES = ...
STOCK_QUIT = ...
STOCK_REDO = ...
STOCK_REFRESH = ...
STOCK_REMOVE = ...
STOCK_REVERT_TO_SAVED = ...
STOCK_SAVE = ...
STOCK_SAVE_AS = ...
STOCK_SELECT_ALL = ...
STOCK_SELECT_COLOR = ...
STOCK_SELECT_FONT = ...
STOCK_SORT_ASCENDING = ...
STOCK_SORT_DESCENDING = ...
STOCK_SPELL_CHECK = ...
STOCK_STOP = ...
STOCK_STRIKETHROUGH = ...
STOCK_UNDELETE = ...
STOCK_UNDERLINE = ...
STOCK_UNDO = ...
STOCK_UNINDENT = ...
STOCK_YES = ...
STOCK_ZOOM_100 = ...
STOCK_ZOOM_FIT = ...
STOCK_ZOOM_IN = ...
STOCK_ZOOM_OUT = ...
STYLE_CLASS_ACCELERATOR = ...
STYLE_CLASS_ARROW = ...
STYLE_CLASS_BACKGROUND = ...
STYLE_CLASS_BOTTOM = ...
STYLE_CLASS_BUTTON = ...
STYLE_CLASS_CALENDAR = ...
STYLE_CLASS_CELL = ...
STYLE_CLASS_CHECK = ...
STYLE_CLASS_COMBOBOX_ENTRY = ...
STYLE_CLASS_CONTEXT_MENU = ...
STYLE_CLASS_CSD = ...
STYLE_CLASS_CURSOR_HANDLE = ...
STYLE_CLASS_DEFAULT = ...
STYLE_CLASS_DESTRUCTIVE_ACTION = ...
STYLE_CLASS_DIM_LABEL = ...
STYLE_CLASS_DND = ...
STYLE_CLASS_DOCK = ...
STYLE_CLASS_ENTRY = ...
STYLE_CLASS_ERROR = ...
STYLE_CLASS_EXPANDER = ...
STYLE_CLASS_FLAT = ...
STYLE_CLASS_FRAME = ...
STYLE_CLASS_GRIP = ...
STYLE_CLASS_HEADER = ...
STYLE_CLASS_HIGHLIGHT = ...
STYLE_CLASS_HORIZONTAL = ...
STYLE_CLASS_IMAGE = ...
STYLE_CLASS_INFO = ...
STYLE_CLASS_INLINE_TOOLBAR = ...
STYLE_CLASS_INSERTION_CURSOR = ...
STYLE_CLASS_LABEL = ...
STYLE_CLASS_LEFT = ...
STYLE_CLASS_LEVEL_BAR = ...
STYLE_CLASS_LINKED = ...
STYLE_CLASS_LIST = ...
STYLE_CLASS_LIST_ROW = ...
STYLE_CLASS_MARK = ...
STYLE_CLASS_MENU = ...
STYLE_CLASS_MENUBAR = ...
STYLE_CLASS_MENUITEM = ...
STYLE_CLASS_MESSAGE_DIALOG = ...
STYLE_CLASS_MONOSPACE = ...
STYLE_CLASS_NEEDS_ATTENTION = ...
STYLE_CLASS_NOTEBOOK = ...
STYLE_CLASS_OSD = ...
STYLE_CLASS_OVERSHOOT = ...
STYLE_CLASS_PANE_SEPARATOR = ...
STYLE_CLASS_PAPER = ...
STYLE_CLASS_POPOVER = ...
STYLE_CLASS_POPUP = ...
STYLE_CLASS_PRIMARY_TOOLBAR = ...
STYLE_CLASS_PROGRESSBAR = ...
STYLE_CLASS_PULSE = ...
STYLE_CLASS_QUESTION = ...
STYLE_CLASS_RADIO = ...
STYLE_CLASS_RAISED = ...
STYLE_CLASS_READ_ONLY = ...
STYLE_CLASS_RIGHT = ...
STYLE_CLASS_RUBBERBAND = ...
STYLE_CLASS_SCALE = ...
STYLE_CLASS_SCALE_HAS_MARKS_ABOVE = ...
STYLE_CLASS_SCALE_HAS_MARKS_BELOW = ...
STYLE_CLASS_SCROLLBAR = ...
STYLE_CLASS_SCROLLBARS_JUNCTION = ...
STYLE_CLASS_SEPARATOR = ...
STYLE_CLASS_SIDEBAR = ...
STYLE_CLASS_SLIDER = ...
STYLE_CLASS_SPINBUTTON = ...
STYLE_CLASS_SPINNER = ...
STYLE_CLASS_STATUSBAR = ...
STYLE_CLASS_SUBTITLE = ...
STYLE_CLASS_SUGGESTED_ACTION = ...
STYLE_CLASS_TITLE = ...
STYLE_CLASS_TITLEBAR = ...
STYLE_CLASS_TOOLBAR = ...
STYLE_CLASS_TOOLTIP = ...
STYLE_CLASS_TOP = ...
STYLE_CLASS_TOUCH_SELECTION = ...
STYLE_CLASS_TROUGH = ...
STYLE_CLASS_UNDERSHOOT = ...
STYLE_CLASS_VERTICAL = ...
STYLE_CLASS_VIEW = ...
STYLE_CLASS_WARNING = ...
STYLE_CLASS_WIDE = ...
STYLE_PROPERTY_BACKGROUND_COLOR = ...
STYLE_PROPERTY_BACKGROUND_IMAGE = ...
STYLE_PROPERTY_BORDER_COLOR = ...
STYLE_PROPERTY_BORDER_RADIUS = ...
STYLE_PROPERTY_BORDER_STYLE = ...
STYLE_PROPERTY_BORDER_WIDTH = ...
STYLE_PROPERTY_COLOR = ...
STYLE_PROPERTY_FONT = ...
STYLE_PROPERTY_MARGIN = ...
STYLE_PROPERTY_PADDING = ...
STYLE_PROVIDER_PRIORITY_APPLICATION = ...
STYLE_PROVIDER_PRIORITY_FALLBACK = ...
STYLE_PROVIDER_PRIORITY_SETTINGS = ...
STYLE_PROVIDER_PRIORITY_THEME = ...
STYLE_PROVIDER_PRIORITY_USER = ...
STYLE_REGION_COLUMN = ...
STYLE_REGION_COLUMN_HEADER = ...
STYLE_REGION_ROW = ...
STYLE_REGION_TAB = ...
TEXT_VIEW_PRIORITY_VALIDATE = ...
TREE_SORTABLE_DEFAULT_SORT_COLUMN_ID = ...
TREE_SORTABLE_UNSORTED_SORT_COLUMN_ID = ...

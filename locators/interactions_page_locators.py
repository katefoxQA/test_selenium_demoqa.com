from selenium.webdriver.common.by import By

class SortablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'a[id="a"]')
    TAB_GRID = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    ITEM_LIST = (By.CSS_SELECTOR, 'div[class="vertical-list-container mt-4"] div[class="list-group-item list-group-item-action"]')
    ITEM_GRID = (By.CSS_SELECTOR, 'div[class="create-grid"] div[class="list-group-item list-group-item-action"]')

class SelectablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    TAB_GRID = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    ITEM_LIST = (By.CSS_SELECTOR, 'ul[id="verticalListContainer"] li[class="mt-2 list-group-item list-group-item-action"]')
    ITEM_GRID = (By.CSS_SELECTOR, 'div[id="gridContainer"] li[class="list-group-item list-group-item-action"]')
    ITEM_LIST_ACTIVE = (By.CSS_SELECTOR, 'ul[id="verticalListContainer"] li[class="mt-2 list-group-item active list-group-item-action"]')
    GRID_LIST_ACTIVE = (By.CSS_SELECTOR, 'div[id="gridContainer"] li[class="list-group-item active list-group-item-action"]')

class ResizablePageLocators:
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, 'div[class="constraint-area"] span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE_BOX = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')
    RESIZABLE = (By.CSS_SELECTOR, 'div[id="resizable"]')
    RESIZABLE_HANDLE = (By.CSS_SELECTOR, 'div[id="resizable"] span[class="react-resizable-handle react-resizable-handle-se"]')

class DroppablePageLocators:
    # Simple
    TAB_SIMPLE = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-simple"]')
    DRAG_ME_SIMPLE = (By.CSS_SELECTOR, 'div[id="draggable"]')
    DROP_HERE_SIMPLE = (By.CSS_SELECTOR, 'div[id="simpleDropContainer"] div[id="droppable"]')

    # Accept
    ACCEPT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-accept"]')
    ACCETABLE = (By.CSS_SELECTOR, 'div[id="acceptable"]')
    NOT_ACCETABLE = (By.CSS_SELECTOR, 'div[id="notAcceptable"]')
    DROP_HERE_ACCEPT = (By.CSS_SELECTOR, 'div[id="acceptDropContainer"] div[id="droppable"]')

    # Prevent Propogation
    PREVENT_PROPOGATION_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-preventPropogation"]')
    DRAG_ME_PREVENT = (By.CSS_SELECTOR, '#ppDropContainer #dragBox')
    NOT_GREEDLY_DROP_BOX_TEXT = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"] p:nth-child(1)')
    NOT_GREEDLY_INNER_BOX = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"]')
    GREEDLY_DROP_BOX_TEXT = (By.CSS_SELECTOR, 'div[id="greedyDropBox"] p:nth-child(1)')
    GREEDLY_INNER_BOX = (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"]')

    #Revert Draggable
    REVERT_DRAGGABLE_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-revertable"]')
    WILL_REVERT = (By.CSS_SELECTOR, '#revertable')
    NOT_REVERT = (By.CSS_SELECTOR, '#notRevertable')
    DROP_HERE_REVERT = (By.CSS_SELECTOR, 'div[id="revertableDropContainer"] div[id="droppable"]')

class DraggablePageLocators:
    SIMPLE_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-simple"]')
    DRAG_ME = (By.CSS_SELECTOR, 'div[id="dragBox"]')

    AXIS_RESTRICTED_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-axisRestriction"]')
    ONLY_X = (By.CSS_SELECTOR, '#restrictedX')
    ONLY_Y = (By.CSS_SELECTOR, '#restrictedY')


import {React} from "react"
import "./UIBar.css"

/**
 * The UI bar at the top the webpage, can be used as info container
 * @return the html of the UI bar
 */
function UIBar() {
    return(
        <div>
            <div className = "UIBarWrapper">
                <div className = "titleWrapper">
                    <span style={{top:"19px",position:"relative"}}>Data Workbench</span>
                </div>
            </div>
        </div>
    )
}
export default UIBar;
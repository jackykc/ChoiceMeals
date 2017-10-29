import React from 'react'

class LogoutView extends React.Component {
	handleClick() {
		localStorage.removeItem('token')
		window.location.replace('/')
	}
	render() {
		return (
			<div>
				<h1>LogoutView</h1>
				<button onClick={() => this.handleClick()}>Logout</button>
			</div>
		)
	}
}

export default LogoutView
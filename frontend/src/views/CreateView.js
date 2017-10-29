import React from 'react'
import { Link } from 'react-router-dom'
import { graphql } from 'react-apollo'
import gql from 'graphql-tag';

const query = gql`
{
  currentUser {
    id
  }
}
`

class CreateView extends React.Component {
	componentWillUpdate(nextProps) {
		if(!nextProps.data.loading && nextProps.data.currentUser === null) {
			console.log("nothing")
			// window.location.replace('/login/')
		}
	}

  	render() {
  		let {data} = this.props
  		if(data.loading) {
  			return <div>Loading...</div>
  		}
    	return <div>CreateView</div>
  	}
}

CreateView = graphql(query)(CreateView)
export default CreateView
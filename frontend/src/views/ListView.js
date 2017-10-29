import React from 'react'
import { Link } from 'react-router-dom'
import { graphql } from 'react-apollo'
import gql from 'graphql-tag';

const USER_QUERY = gql`
query {
  allIngredients {
    id
    name
    category {
      id
      name
    }
  }
}
`;


console.log(USER_QUERY);

class ListView extends React.Component {

    render() {
        console.log(this.props);
    	let { data } = this.props
    	if (data.loading || !data.USER_QUERY) {
      		return <div>Loading...</div>
    	}
    	return (
    		<div>
    			{data.allMessages.map(item=> (
    				<p key={item.id}>
    					<Link to={`/names/$(item.id)/`}>
    						{item.name}
    					</Link>
    				</p>
				))}
			</div>
    	)
    }
}

ListView = graphql(USER_QUERY)(ListView)

export default ListView